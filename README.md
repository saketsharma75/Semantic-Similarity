# Word Similarity Analysis with Spacy

This code uses Spacy, a natural language processing library, to analyze the similarity between different words and sentences. Specifically, it loads the 'en_core_web_md' language model to generate word vectors, which are used to calculate similarity scores between words and sentences.

## Usage
To run this code, you will need to have Spacy installed on your system. Once installed, you can simply run the script to see the output.

The code includes two main sections. The first section generates similarity scores between individual words, specifically "cat," "monkey," and "banana." The second section generates similarity scores between sentences, specifically a given sentence and a list of other sentences.

## Interesting Findings
The author of this code found it interesting that the similarity scores are based on the contextual meaning of the words, rather than just their surface-level similarity in spelling or pronunciation. As an example, they provided the words "apple" and "orange," which are often compared or contrasted with each other because they are both types of fruit.

## Differences Between Language Models
The code notes that when the simpler language model 'en_core_web_sm' is used instead of 'en_core_web_md,' the similarity scores are lower. This is because the 'en_core_web_md' model has more information about the words and their meanings, which allows it to make more accurate similarity scores. Additionally, the output includes a warning that the simpler model has no word vectors loaded, which may not give useful similarity judgments.
