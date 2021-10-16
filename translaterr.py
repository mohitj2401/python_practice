from googletrans import Translator
import json


translator = Translator()
key_value = {

    "home": "Home",
    "videos": "Videos",
    "categories": "Categories",
    "profile": "Profile",


    "welcome to": "Welcome to",
    "sign in to continue": "Sign In to Continue",
    "skip": "Skip",
    "done": "Done",

    "intro-title1": "Explore Latest News",
    "intro-title2": "Get Notified First",
    "intro-title3": "Save Articles",
    "intro-description1": "Explore lattest news and events happening in the world in minutes...",
    "intro-description2": "Subscribe and get notified to all of our articles & share with your friends...",
    "intro-description3": "Bookmark, like & comment on your favourite articles and share on social media...",
    "get started": "Get Started",
    "don't have social accounts?": "Don't have social accounts?",
    "continue with email >>": "Continue with Email >>",

    "sign up": "Sign Up",
    "sign in": "Sign In",
    "follow the simple steps": "Follow the simple steps",
    "name": "Name",
    "already have an account?": "Already have an account?",
    "forgot password?": "Forgot Password?",
    "reset your password": "Reset Your Password",
    "submit": "Submit",
    "sign in successful!": "Sign In Successful!",
    "sign up successful!": "Sign up successful!",
    "don't have an account?": "Don't have an account?",



    "search news": "Search News",
    "popular news": "Popular News",
    "recent news": "Recent News",
    "explore": "Explore",
    "featured": "Featured",
    "view all": "view all",

    "video articles": "Video Articles",
    "most recent": "Most Recent",
    "most popular": "Most Popular",
    "no categories found": "No categories found",





    "people like this": "People like this",
    "you might also like": "You might also like",
    "no articles found": "No articles found",



    "no internet": "No internet connection!",
    "no comments found": "No comments found",
    "be the first to comment": "Be the first to comment",


    "recent searchs": "Recent Searchs",
    "search-description":  "You haven't search for any items yet.\n Try now - we will help you!",
    "we have found": "We have found",
    "try again": "Try again!",




    "bookmarks": "Bookmarks",
    "sign in first": "Sign In First",
    "sign in to save your favourite articles here": "Sign in to save your favourite articles here",
    "save your favourite articles here": "Save your favourite articles here",




    "check your internet connection!": "Check your internet connection!",
    "something is wrong. please try again.": "Something is wrong. Please try again.",
    "error fb login": "Error with facebook login! Please try with google",



    "cancel": "Cancel",
    "no sign in title": "Sign in first to access this feature",
    "no sign in subtitle": "You haven't signed in yet. Please sign in to unlock this feature",



    "comments": "Comments",
    "write a comment": "Write A Comment",



    "no content": "No contents found",
    "flag this comment": "Flag this comment",
    "unflag this comment": "Unflag this comment",
    "report": "Report",
    "delete": "Delete",
    "report-info": "Your report has been sent succesfully to the admins",
    "report-info1": "Thanks for your report. We will reponse within 24 hours.",
    "report-guest": "Sign In is Required!",
    "report-guest1": "You have to sign in to report about any comments",
    "comment flagged": "This comment has been flagged!",


    "notifications": "Notifications",
    "notification details": "Notification Details",
    "custom notifications": "Custom Notifications",
    "news notifications": "News Notifications",
    "no notification": "No notifications found",



    "general settings": "General Settings",
    "dark mode": "Dark Mode",
    "login": "Login",
    "get notifications": "Get Notifications",
    "contact us": "Contact Us",
    "rate this app": "Rate this app",
    "licence": "Licence",
    "privacy policy": "Privacy Policy",
    "about us": "About Us",
    "logout": "Logout",
    "edit profile": "Edit Profile",
    "update profile": "Update Profile",
    "updated successfully": "Updated Successfully",
    "enter new name": "Enter new name",

    "logout title": "Do you really want to logout from the app?",
    "yes": "Yes",
    "no": "No",

    "language": "Language",
    "select language": "Select Language",

    "buy now": "Purchase this app",
    "buy now subtitle": "Buy the full source code here"



}
new_dec = {}
# print(key_value)

for text in key_value:

    result = translator.translate(key_value[text], dest='te')
    new_dec[text] = result.text

print(new_dec)
with open("sample1.json", "w") as outfile:
    json.dump(new_dec, outfile)
