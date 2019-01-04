Update 01/2019: Keeping this code here for reference, this interface has turned into an IUI 2019 paper https://arxiv.org/abs/1810.09648


# Interactive UI for Human-in-The-Loop Question Answering

This is an interactive user interface for studying how humans handle information given to them in a live setting by computers. It focuses on the the domain of quiz bowl, where players can "buzz" in at any time and answer trivia based questions. The computer system is based on [QANTA](https://github.com/Pinafore/qb), a deep-learning Question Answering system.

This interface is useful for exploring how computers can provide humans with helpful resources, feedback, and hints in a live setting without overwhelming them with information. It has applications in translation systems, reading comprehension, question answering, and other NLP related tasks.

The following goes over the code and how to set it up on your own machine.

## Installation

To use the interface and code make sure you have [QANTA](https://github.com/Pinafore/qb) installed. Follow the directions there to get started.

Once QANTA is installed, clone the repo onto your machine and install the requirements.
```
git clone https://github.com/ihsgnef/qb_interface.git
cd qb_interface
pip install -r requirements.txt
```

Now you need to get the data, preprocess it, download the pretrained models, and cache their results

TODO THIS PART.
