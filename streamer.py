import json

from twisted.internet import reactor

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS

from util import MSG_TYPE_NEW, MSG_TYPE_RESUME, MSG_TYPE_EOQ, \
        MSG_TYPE_BUZZING_REQUEST, MSG_TYPE_BUZZING_ANSWER, \
        MSG_TYPE_BUZZING_GREEN, MSG_TYPE_BUZZING_RED

class StreamerProtocol(WebSocketClientProtocol):

    def onOpen(self):
        self.qid = None
        self.text = None
        self.position = 0
        self.length = 0
        
    def new_question(self, msg):
        self.qid = msg['qid']
        self.text = msg['text']
        if isinstance(self.text, str):
            self.text = self.text.split()
        self.length = len(self.text)
        self.position = 0
        msg = {'type': MSG_TYPE_NEW, 'qid': self.qid}
        self.sendMessage(json.dumps(msg))

    def update_question(self, msg):
        if msg['qid'] != self.question['qid']:
            raise ValueError("[streamer] inconsistent qids")
        self.position += 1
        if self.position < self.length:
            msg = {'type': MSG_TYPE_RESUME, 'text': self.text[self.position],
                    'qid': self.qid, 'position': self.position}
        else:
            msg = {'type': MSG_TYPE_EOQ, 'text': self.text[self.position],
                    'qid': self.qid, 'position': self.position}
        self.sendMessage(json.dumps(msg))
            

    def onMessage(self, payload, isBinary):
        msg = json.loads(payload)
        if msg['type'] == MSG_TYPE_NEW:
            self.new_question(msg)
        elif msg['type'] == MSG_TYPE_RESUME:
            self.update_question(msg)

if __name__ == '__main__':
    factory = WebSocketClientFactory(u"ws://127.0.0.1:9000")
    factory.protocol = MessageBasedHashClientProtocol
    connectWS(factory)
    reactor.run()
