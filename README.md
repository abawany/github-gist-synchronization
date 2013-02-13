# Automated Github Gist Generation
## by Ali Bawany and Mike Kojder

## Summary:
Gist is a facility provided by GitHub to store sample code segments in GitHub and then show them on your site. One use of this facility is for building technology tutorials: the host site can contain Gist links that show the relevant samples of code; when the Gist link changes, all of the refererring sites automatically show the updated code. We built a solution where a developer can pick code segments from his/her existing code base and then run our tool to extract these segments and update the Gists. This ensures that the Gists are always in sync with actual working code and that the developer only has to update the code in one location to keep all of their tutorials up to date. 

## Description:
Github Gist provides a way to share snippets of code with others: examples can be seen at https://gist.github.com/gists. The snippets are hosted, formatted, and revision-controlled by Github ensuring that a developer can add these links to his/her site when illustrating a point or building an online tutorial for a new technology; an example is at https://www.x.com/developers/paypal/forums/website-payments-standard/return-url-parameters-missing#answer-215428 . These Gists are revision controlled, enabling the originator to update the code segment in one location and then have all the sites that use this Gist to be automatically updated. 

The main problem with Gist is that the code segments exist independently of the developer's main codebase. Thus, if you had some sample code in a Git repository, to make Gists you would cut-and-paste code from this repo. This results in the case where updates to your Git repo are not reflected in Gist, reducing the utility of the latter. 

We wanted to build a solution to make it easier to keep both sources in sync. We built a tool and process as follows to solve this problem. The developers marks, via comments, the segments of his/her code that should be served as Gists. He/she also creates placeholder Gists at https://gist.github.com. Then the tool we built needs to be configured to know about Gists that were pre-created and the developer's Github login details. Once this is done and the tool is run, it will extract the Gists from the developer's code and post them to GitHub. Anytime the developer changes the relevant segments in his main codebase, he can re-run the tool and in one shot, update all of his relevant Gists. Thus this is a great time saving tool, which will also ensure that all of the tutorials and external references to code samples always remain in sync with the main codebase. The instructions to use this tool (jistScript.py) are as follows:

### Instructions:

* Install jist as follows:
```
gem install jist
```

* If you are going to use the library in your application, add the following to the Gemfile:
```
source :rubygems
gem 'jist'
```

* Enter your login credentials for your Gist account as follows:
```
jist --login
```

* Create the initial Gist on Github.  None of the initial settings matter EXCEPT the filename; make sure that the filename follows this convention: GIST_yourFileNameHere.json

* Open jistScript.py in a text editor.  The top line contains a map.  Set up the map so that the key is the youFileNameHere from the previous step and the value is your Gist's ID.  (e.g. "yourFileNameHere" : "129ccbc3a8ae325638e9")

* In the code file that contains the relevant Gist, insert GIST_START on the line above the desired text, followed by a space or spaces and yourFileNameHere.  On the line after desired text, insert GIST_END. If code, it is recommended that these be comments.

#### Ruby code example:
```ruby
...
#GIST_START yourFileNameHere
print "This is what I want to appear in the Gist"
print "Also this too"
#GIST_END
...
```

#### Java code example:
```java
...
// GIST_START yourFileNameHere
System.out.println("This is what I want to appear in the Gist");
System.out.println("Also this too");
//GIST_END
...
```

* Run the python script with the files that contain your Gist as arguments, as follows:
```
python jistScript.py file1.txt file2.java
```

## Conclusion:
Existing solutions require developers to cut and paste from their existing code to build GitHub Gists, which results in two sources of truth that must be manually synchronized. Our solution allows the developer to mark segments within his/her code that are to be made into Gists. Whenever the main code is updated, running our tool will generate and upload new Gists to GitHub, ensuring that the Gists they are using for tutorials and etc. are always up to date. Thus, this tool reduces manual labor, improves developer efficiency, and improves the experience of the users of the Gists in that it assures them that the Gists they looking at are up to date. Hope it helps you.

## References: 
- We used https://github.com/ConradIrwin/jist as a utility within the tool to submit the extracted Gists to Github Gist.
