**********
UI testing
**********

``selenium``
============
* http://www.seleniumhq.org/

Selenium automates browsers. That's it! What you do with that power is entirely up to you. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

Selenium 1.0 + WebDriver = Selenium 2.0

* WebDriver is designed in a simpler and more concise programming interface along with addressing some limitations in the Selenium-RC API.
* WebDriver is a compact Object Oriented API when compared to Selenium1.0
* It drives the browser much more effectively and overcomes the limitations of Selenium 1.x which affected our functional test coverage, like the file upload or download, pop-ups and dialogs barrier
* WebDriver overcomes the limitation of Selenium RC's Single Host origin policy

WebDriver is the name of the key interface against which tests should be written in Java, the implementing classes one should use are listed as below:

    * ChromeDriver,
    * EventFiringWebDriver,
    * FirefoxDriver,
    * HtmlUnitDriver,
    * InternetExplorerDriver,
    * PhantomJSDriver,
    * RemoteWebDriver,
    * SafariDriver.

.. figure:: img/selenium-ide.png
    :align: center
    :width: 75%

