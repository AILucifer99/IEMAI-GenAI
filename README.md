## AI Lingualistic Hub Powered by Google Gemini Multi-Modal Large Language Model.

An implementation of end to end AI lingualistic ecosystem with Google Gemini Model. The project deals with many features like AI Blog Generation, AI Text Summarization, Paraphrasing and many more. The entire system is using Google Gemini Large Language Model to solve the respective tasks. 

### Application Home Page
![Gemini Multilingual Studio](https://github.com/AILucifer99/Gemini-Multilingual-Studio/blob/main/assets/Application.png?raw=true)


### Parameters in the GUI
The system is designed in such a way that an end user can control the generation of the Gemini Large Language Model. So, many parameters are also provided in the GUI for the controlling. The parameters are consistent throughout the GUI. 
1.   *Temperature* - The sampling temperature for text generation affects how predictable the output is; higher values make it less predictable. Avoid adjusting both temperature and top_p simultaneously.
2.   *Top P Sampling* - The top-p sampling mass for text generation determines the probability mass considered. For example, with top_p = 0.2, only tokens with a cumulative probability of 0.2 are sampled. Avoid adjusting both temperature and top_p simultaneously.
3.   *Max New Tokens* - The maximum number of tokens to generate in a single call. The model will stop generating when it reaches this limit.

#### These three parameters are the main controlling components of the Gemini Model, so tuning these values can help a lot in generating variety of outputs for the same prompt and thus, the generation can be much more relieable and robust. 
