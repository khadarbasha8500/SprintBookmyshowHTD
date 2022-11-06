#Feature: signin by apple id
#
#  Background: signin the book my shoe by using the valid apple id
#    Given user able to launch browser
#    When user able to click on signin button
#    Then user able to click on the continue with apple
#
#  Scenario Outline:
#    When user enter the  apple id "<apple_id>"
#    And user click on the next icon
#    Then user enter the apple id password "<password>"
#    And  user click on the next button
#
#    Examples:
#    |apple_id|             |password|
#    |khadar123@icloud.com| |122455|
#    |sai123@gmail.com    | |sai123|
#    |raj987@icloud.com   | |cloud12|
#    |pavan@email.com     | |12busu |
#    |hussain1@icloud.com | |khadar |
