# ChatGPT-Linux
Greetings, this is basically an initiative to introduce ChatGPT into native linux terminals. The whole idea and concept is about having an AI that is dedicated to linux and its various distributions. Just imagine of having an AI like ChatGPT or even ChatGPT itself inside your linux that you can operate with your terminal. So, to begin with...

Note:
-----	 
This is program which you can run both in Linux and Windows. 
For windows users, you can simply run the code, if you have a python interpreter installed in your system.
Download the python interpreter from this link: https://www.python.org/downloads/ if you don't have it. 
Most of the Linux distributions come with a pre-installed python interpreter. So I believe there is no need for this extra step, if you are using Linux.

Step - 1: (Setting up the environment)
--------------------------------------
1. As mentioned in the note. Of course a python interpreter (recommended: latest version) is required. So make sure you have it installed.
2. After installing the interpreter, open you Linux terminal and type 

```
pip install openai
``` 
to install the Open Ai library. [Windows users can use their power shell or command prompt].

3. The library should be installed at ```/home/user/.local/bin```
4. You might see a warning message, but don't worry that's what we are going to handle next.

Step - 2: (Configuring your terminal)
---------------------------------------------------
Note: Windows Users skip this step.
 
1. Once you are done installing the library, depending on your Linux distribution you will be using a ~/.bashrc or a ~/.zshrc terminal. Check whether you are using a ~/.bashrc or a ~/.zshrc terminal.  
2. Next, type 
```
nano ~/.bashrc
``` 
or,
```
nano ~/.zshrc
``` 
(depends on your terminal type) in your terminal. And go the very bottom of the configuration script.

3. Add this statement 
```
export PATH=$PATH:/home/storm/.local/bin
``` 
to the bottom of the script. Here you are actually letting your terminal know about the openai library you have just installed and also where it is located at.

4. Save the script and safely exit. Do be careful about making changes in the terminal script (~/.bashrc or ~/.zshrc).
5. Type 
```
source ~/.bashrc
``` 
or,

```
source ~/.zshrc
``` 
in order to activate the changes.

Step - 3: (Getting Your OpenAI API key)
----------------------------------------
Note: Windows Users skip point - (4 and 5)

1. It is required to have an Open AI account. Create an account if you don't have it to proceed further.
2. You are going to be needing an API key which will connect the program with the Open AI servers.
3. Follow this link: https://platform.openai.com/account/api-keys to generate your own API key. Of course you are going to keep it a secret and save it for future uses.
4. Once you have generated your API key, open your terminal, type 
```
nano ~/.bashrc
``` 
or, 
```
nano ~/.zshrc
``` 
again and add 
```
export OPENAI_API_KEY=[Your OpenAI API Key]
``` 
to the very bottom of the script. Just below the previous change you have made.

5. Type 
```
source ~/.bashrc
``` 
or, 
```
source ~/.zshrc
``` 
in order to activate the changes again. 

[For Windows Users]
-------------------
1. After generating the API key, open chatGPT.py in any text editor or IDE.
2. Find this line of code, 
```python
openai.api_key = os.environ["OPENAI_API_KEY"]
``` 
from chatGPT.py

3. Alter this line to 
```python
openai.api_key = "[Your Open AI API key]"
``` 
4. Just copy and past the generated key within the quotation.
5. Save it

[WE HAVE COME THIS FAR. I believe you should be able to run the program now.]

Step - 4: (Creating Your own Custom Alias)
------------------------------------------
Note: Optional Step for Linux Users.

1. You can create your custom Alias in order to rum the program. This just puts an extra flavor to your Linux environment as if it is your native application.
2. If you don't know how to do it, simply go to your terminal and type 
```
nano ~/.bashrc
``` 
or, 
```
nano ~/.zshrc
```
3. Add this statement 
```
alias [Your Preferred call/command]="[instructions to execute/run chatGPT.py ]"
``` 
to the very bottom of the script. Example: ```alias ChatGPT="/path/to/your/directory && python chatGPT.py"```

4. Save the script and safely exit.
5. Type 
```
source ~/.bashrc
``` 
or, 
```
source ~/.zshrc
``` 
in your terminal in order to activate the changes again.

That's all for the instructions. I pray and hope that you all will use the program and make the best uses out of it. "Believe in open-source. Keep it open-source. Free fall...Deep Dive into the world of innovations."

Wish you all the very best.

Thank You.

## Best Regards,
Syed Golam Abid
AKA Storm Hellsing
