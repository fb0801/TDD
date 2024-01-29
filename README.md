# TDD
TDD

Project to learn TDD with python 

# Changes made:

# Issues:
-Geckodriver not being found solved by finding where its saved and using path

-Geckodriver not working fixed by adding to path, ensure you follow Prerequisites and Assumptions section of book

-url decripted so instead use re_path in script

-AttributeError: 'WebDriver' object has no attribute 'find_element_by_tag_name' -> need to change to find_element(By.TAG_NAME,'h1').text as 'find_element_by_tag_name' no longer works

- ran into git issues resulting in some repo loss

- No module named 'django.core.urlresolvers' -> resoloved using from django.urls import reverse

# Resouces used:

http://www.obeythetestinggoat.com/

original repo -> https://github.com/hjwp/book-example

https://www.browserstack.com/guide/geckodriver-selenium-python

https://www.obeythetestinggoat.com/book/pre-requisite-installations.html

https://selenium-python.readthedocs.io/

https://www.djangoproject.com/

https://www.toptal.com/developers/gitignore/

https://www.atlassian.com/git/tutorials/saving-changes/gitignore

https://www.freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git/

https://www.browserstack.com/guide/geckodriver-selenium-python

https://stackoverflow.com/questions/42524114/how-to-install-geckodriver-on-a-windows-system

https://stackoverflow.com/questions/40388503/how-to-put-geckodriver-into-path

https://www.youtube.com/watch?v=Xjv1sY630Uc

https://www.youtube.com/watch?v=j7VZsCCnptM

https://www.browserstack.com/guide/geckodriver-selenium-python#:~:text=Click%20New%20in%20the%20Edit,located%20in%20C%3A%5CDRIVERS.

https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to

https://www.selenium.dev/documentation/webdriver/elements/finders/

https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el

https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete

https://stackoverflow.com/questions/25964312/not-null-constraint-failed-after-adding-to-models-py

https://12factor.net/

https://hynek.me/talks/python-deployments/

https://www.git-tower.com/learn/git/faq/track-remote-upstream-branch

https://www.git-tower.com/learn/git/faq/git-rename-master-to-main

https://www.selenium.dev/documentation/webdriver/elements/finders/

https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers

https://www.selenium.dev/documentation/webdriver/elements/locators/#css-selector

https://qunitjs.com/intro/

https://releases.jquery.com/qunit/

https://jquery.com/download/

https://pypi.org/project/python-dotenv/

https://www.runthat.blog/how-to-create-and-use-env-files-in-python/

https://ioflood.com/blog/python-dotenv-guide-how-to-use-environment-variables-in-python/

https://stackoverflow.com/questions/37525075/what-does-tests-module-incorrectly-imported-mean