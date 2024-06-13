<div align="center">

# <span style="color: #555;">System Prompt Generator in ShareGPT format</span>

<hr>
## - and a couple of other useful little python scripts. 🙂

### <span style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 6em;"><b>This is a simple Python workflow to generate system prompts in the [ShareGPT format](https://guide.repleteai.com/Text-Generation/Prompt-Templates/ShareGPT), along with some other helpful simple scripts you might need. </b></span>

<hr>
I ended up using this to create [Pneuma](https://huggingface.co/Replete-AI/Pneuma), which is a series of models that have been trained on data representing experiences and interactions. I generated the conversations and found some regularization data on huggingface which I reformatted and then combined with the data I generated. However, all datasets just use a basic "You are an AI assistant" system prompt. I don't like that, I don't need an assistant...so I needed to change the system prompt to something a little more creative and fun. Of course, this script can be modified to generate any kind of system prompt you want.

<hr>

</div>

### Note: This script is made for ShareGPT format data. Make sure your data is in this format before trying to change your system prompts. Here's an example of the data I used:

```json
{"conversations": [{"from": "system", "value": "..."}, {"from": "human", "value": "How can I create a class in Python that takes the name and age of a person as arguments and prints a greeting?"}, {"from": "gpt", "value": "To create a class that takes the name and age of a person as arguments and prints a greeting, you can define a class called \"Person\" with an \"__init__\" method and a \"greeting\" method. The \"__init__\" method will initialize the name and age attributes of the person, and the \"greeting\" method will print a greeting message using the name and age.\n\nHere's an example code:\n\n```python\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    \n    def greeting(self):\n        print(\"Hello, my name is \" + self.name + \" and I am \" + str(self.age) + \" years old.\")\n\nperson1 = Person(\"John\", 20)\nperson1.greeting()\n```\n\nIn this code, we define the \"Person\" class with the \"__init__\" method that takes two arguments: \"name\" and \"age\". Inside the \"__init__\" method, we assign the \"name\" argument to the \"name\" attribute of the class instance (self), and the \"age\" argument to the \"age\" attribute. \n\nThe \"greeting\" method is defined to print a greeting message using the \"name\" and \"age\" attributes. We use string concatenation to combine the greeting message with the values of the \"name\" and \"age\" attributes.\n\nTo create an instance of the \"Person\" class, we create the \"person1\" object and pass the name \"John\" and age 20 as arguments to the class constructor. Then, we call the \"greeting\" method on the \"person1\" object to print the greeting message.\n\nThe output of the code will be:\n```\nHello, my name is John and I am 20 years old.\n```"}]}
```
As you can see, the system prompt is just an elipse, but with this script, you can transform any system prompt. 🙂

The main reason I created this script is because my data didn't have system prompts at all, so I had to use ctrl+f to replace the beginnings of each line with empty system strings.

## How to use the script

First, you want to use git to clone the repository and then run `pip install -r requirements.txt`

It's just going to install openai, as that's all this script needed. You might need to follow instructions in your terminal to get a specific version of openai.

### Optional split.py script

If you have an insanely large dataset, it might help to use split.py to divide them out evenly into ten separate files and then copy your system.py file a couple of times. This way you can triple the speed of the generations across different accounts with different API keys.

### API key

In line 7, place your Together.ai API key into the quotes.

### Specify the path to your dataset

In line 13, paste the path to your dataset on your machine in the quotes.

### Create an output file and specify it

Create an output.jsonl file and then paste the location of it into the quotes on line 47.

### Modify the system prompt

As I said earlier in this readme, I made this script for a model called Pneuma, so in line 28 you will want to modify the system prompt from the one that I was using.

### Specify the model you'd like to use

I used meta-llama/Llama-3-70b-chat-hf for the generation of my system prompts. It's kind of expensive and can probably be done just as well with a different model, if you'd like.

### Test the script

You wanna make sure that your system prompt is good for your use case. So, I'd take like 5-10 lines of your original dataset, make a test_dataset.jsonl file, and set that as your input file. Then I'd run `system.py` in my terminal and if it's set up properly, there will be a little progress bar in the terminal to keep you updated on the job. If you're happy with the system prompts it generated for you, then feel free to try it with your whole dataset.

### Extra scripts

I included a script to count the amount of tokens in the dataset, as well as a script to shuffle the lines in the dataset, named mixup.py.

I created mixup.py because my regularization data is a combination of like 7 different datasets, and I wanted them to be properly mixed up so that it would work properly as regularization. If I didn't do this it would be more like training with different datasets enabled in axolotl rather than using one big dataset.

I also have a dataset to reformat DPO data into instruct data so that you can use datasets like Intel/orca_dpo_pairs as your regularization data. Also their rejected outputs in that dataset are really low quality so it honestly works better as just instruct data, anyways.
The combine script is for if you split your dataset up, like I did. I used it to combine the folder I was storing my final dataset shards in. Then I used mixup.py to shuffle the lines of the combined dataset a couple of times.

## Enjoy!
