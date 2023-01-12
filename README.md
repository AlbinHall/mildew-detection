![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Gitpod Template Instructions

Welcome,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the Use this template button to get started.

You can safely delete the Gitpod Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Gitpod Template Instructions at least once, though! It contains some important information about Gitpod and the extensions we use. 

## Gitpod Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* It is excpected that the leaf with mildew will be detected through its destinct spots caused by the mildew deasese.
* The validation will be made thorugh comparision with a healthy leaf(Image study)


## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Data Visualization

* We will display the "mean" and "standard deviation" images for healthy and mildew infected leaf's.
* We will display the difference between an average healthy leaf and an average mildew infected leaf.
* We will display a image montage for either healthy or mildew infected leaf.

### Business Requirement 2: Classification

* we want to predict if an leaf is infected with mildew or not.
* We want to build a binary classifier and generate reports.


## ML Business Case

### MalariaClf

* We want a ML model to predict if a leaf is infected with mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our ideal outcome is provide the farm team a faster and reliable diagnostic if a given leaf/tree is infected or not with mildew.
* The model success metrics are
Accuracy of 97% or above on the test set.
* The model output is defined as a flag, indicating if the leaf has mildew or not and the associated probability of being infected or not. The farm staff will do collect the lleafs as usual and upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected or uninfected leafs. A leaf sample is collected, mixed with a reagent and examined under the microscope. Visual criteria are used to detect mildew. It leaves room to produce inaccurate diagnostics due to human errors And takes alot of time. 
* The training data to fit the model come from Code institute and was found the kaggle Website. This dataset contains about FIX THIS. We have extracted a subset of 5643 images from this dataset and saved it to kaggle dataset directory for quicker model training.
Train data - target: infected or not; features: all images

FIXING THIS AND THE UPPER IN THE PROJECT
## Dashboard Design
* Page 1: Quick Project Summary
Quick project summary
General Information
Mildew is an fungus that can infect the leafs of the cherry tree.
A leaf from the cherry tree is collected. Visual criteria are used to detect mildew infection.
The mildew infection is devistating to the cherry tree farmers and takes alot of time for the farm workers to detect and handle
Project Dataset
The available dataset contains 5643 out of +27 thousand images taken from blood smear workflow (when a drop of blood it taken on a glass slide) of cells that are parasitized or uninfected with malaria.
Link to addition ainformation
Business requirements
The client is interested to have a study to visually differentiate between a parasite contained and uninfected cell.
The client is interested to tell whether a given cell contains malaria parasite or not.
Page 2: Cells Visualizer
It will answer business requirement 1
Checkbox 1 - Difference between average and variability image
Checkbox 2 - Differences between average parasitized and average uninfected cells
Checkbox 3 - Image Montage
Page 3: Malaria Detector
Business requirement 2 information - "The client is interested to tell whether a given cell contains malaria parasite or not."
Link to download a set of parasite contained and uninfected cell images for live prediction.
User Interface with a file uploader widget. The user should upload multiple malaria cell image. It will display the image and a prediction statement, indicating if the cell is infected or not with malaria and the probability associated with this statement.
Table with image name and prediction results.
Download button to download table.
Page 4: Project Hypothesis and Validation
Bloack for each project hypothesis, describe the conclusion and how you validated.
Page 5: ML Performance Metrics
Label Frequencies for Train, Validation and Test Sets
Model History - Accuracy and Losses
Model evaluation result

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
