# Analysis of Rumours for Delhi Riots

Homework Assignment for the course CSE648: Privacy and Security in Online Social Media taken by Dr. Ponnurangam Kumaraguru at IIIT Delhi during the Winter 2020 Semester.

## Premise

Our task was to identify, reduce, and deter the effect of rumors through Twitter, as tweeted mentioning the official handles of Delhi Police during Delhi Riots in February, 2020. We developed a model to identify rumours using an SVM and formulated a spread score for the same.

## Usage Guide

Following is a quick set up guide:

+ Ensure that all files - model SVM.sav, police.py, requirements.txt are present in the same folder. Within the same folder make a credentials.py file and save api_key, access_token under the following variable names:

    ```api_key, api_key_secret, access_token, access_token_secret```

+ Within the same folder, open command prompt/terminal and install all requirements needed to run the classification script using the following command:

    ``` pip install -r requirements.txt```

+ Upon installation, run the classification script on the command line:

    ```python police.py```

    The script would require the user to provide the link of the tweet and choose an appropriate category for it from action / help / other / praise / question / report.

    ![photo](https://i.imgur.com/YP0B3LH.png)

+ Upon input of this information, the classifier script yields the following output as result:

    ![photo](https://i.imgur.com/EasIWQL.png)

    Along with the predicted class, it also yields the likelihood of the tweet across all classes.