# Voice-based-Email-service-for-visually-challenged-people
Final Year MCA Project

Abstract
    
    .Due to  simplicity and accessibility, Internet is widely used in almost all the communication applications
    In the recent times,number of application based on internet have been developed to make the communication 
    as a more reliable and efficient in nature.Out of this numerous applications, E-mail is the most widely
    used and reliable way to communicate with each other.
    
    .The usage of e-mail is quiet easy  for regular users but when it comes to the user with visual defect,the
    system is yet very difficult to use. This arises a significant need to upgrade the existing system to make
    it more useful for the visually impaired. 
    
    . Thus,in this Project I used IVR- Interactive voice response, thus enabling everyone to control their mail
    accounts using their voice only and to be able to read,send, and perform all the other useful tasks. The
    system will prompt the user with voice commands to perform certain action and the user will respond to the
    same. 
    
    . The main benefit of this system is that the use of keyboard is completely eliminated,the user will have
    to respond through voice and mouse click only.
    
    .This system will perform actions based on the clicks only that is left click or right click, it does not
    depends on the portion of the screen where the cursor is placed before the click giving user the freedom
    to click blindly anywhere on the screen.
    
Introduction

    Internet is considered as a major storehouse of information in today’s world. No single work can be done
    without the help of it. It has even become one of the de facto methods used in communication. And out of
    all methods available email is one of the most common forms of communication especially in the business
    world. However not all people can use the internet.This is because in order to access the internet you
    would need to know what is written on the screen.If that is not visible it is of no use. This makes internet
    a completely useless technology for the visually impaired and illiterate people. Even the systems that are
    available currently like the screen readers TTS and ASR do not provide full efficiency to the blind people
    so as to use the internet. As nearly 285 million people worldwide are estimated visually impaired it become
    necessary to make internet facilities for communication usable for them also.

    Therefore we have come up with this project in which we will be developing a voice based email system which
    will aid the visually impaired people who are naive to computer systems to use email facilities in a hassle
    free manner. The users of this system would not need to have any basic information regarding keyboard
    shortcuts or where the keys are located. All functions are based on simple mouse click operations making
    it very easy for any type of user to use this system. Also the user need not worry about remembering which
    mouse click operation he/she needs to perform in order to avail a given service as the system itself will
    be prompting them as to which click will provide them with what operations.

Existing System

    1. The existing system uses mainly three type of technologies like
        STT (Speech to Text): here whatever we speak will be converted to text,
        TTS (Text to Speech): this is opposite of STT method, here the text written on the screen will be 
                                read by the system
        
    2. If cursor moves over register icon it would sound register button, after clicking on register button
         it would give a voice notification like you are on registration page
        
    3. After registration, user has to go to login page and type user id & password which will be recognized
        through database enabling the correct user to get access to his/her account
        
    4. Also, there will be an icon for logout, which would read as logout when mouse goes or rolls over it.
         So, when the user wants can logout from the system
        
    5. user should be well versed with the keyboard as to where each and every key is located. A user is new
         to computer can therefore not use this service as they are not aware of the key locations.
        
DisAdvantage
    
    1. The existing system uses mainly  STT (Speech to Text): here whatever we speak will be converted to text
 
    2. User will be very well guided with the help of voice commands, while registering all the necessary fields
         to be filled will be read by site, by clicking on that box he/she would have to fill in them
        
    3. user has to go to login page and type user id & password which will be recognized through database enabling
         the correct user to get access to his/her account
        
    4. the user cannot make use of mouse pointer as it is completely inconvenient if the pointer location cannot
         be traced
    
    5. Not too much friendly for  visually challenged people.

Proposed System

    1. Unlike current system which emphasizes more on user friendliness of normal users, our system focuses
         more on user friendliness of all types of people including normal people visually impaired people
         as well as illiterate people.The complete system is based on IVR- interactive voice response.
        
    2. When using this system the computer will be prompting the user to perform specific operations to avail
         respective services and if the user needs to access the respective services then he/she needs to 
         perform that operation. 
        
    3. One of the major advantages of this system is that user won’t require to use the keyboard. All 
        operations will be based on mouse click events. 
        
    4. This system will be perfectly accessible to all types of users as it is just based on simple mouse
         clicks and speech inputs and there is no need to remember keyboard shortcuts.
       
    5. Also because of IVR facility those who cannot read, need not worry as they can listen to the prompting
         done by the system and perform respective actions

Advantage

    1. The disabilities of visually impaired people are thrashed .
   
    2. This system makes the disabled people feel like a normal user.
   
    3. They can hear the recently received mails.
    
    4. User will be very well guided with the help of voice commands
    
    5. User Friendly

Design

    A. User Interface Design:
        
        The user interface is designed using Adobe Dreamweaver CS3. The complete website focuses more
        on efficiency in understanding the IVR rather than the look and feel of the system as the system
        is primarily developed for the blind people to whom the look and feel won’t be of that primary
        importance as the efficiency of understanding the prompting would be.

    B. Database Design:
        
        Our system maintains a database for user validation and storing mails of the user. There are a total
        of five tables.The relationship between them is assigned after much consideration. The E-R diagram
        of our complete system is depicted The Inbox, Sent-Mail and Trash schemas will store all mails of 
        the respective service that belongs to that particular user.

    C. System Design:
        
        we can see all operations are performed by mouse click events only. Also at some places voice input
        is required.In this phase a complete flow diagram of the working system is designed. This flow diagram
        will show the details of all the events like actions to be performed for an event.
        
   After completion of the design phase, we will now start to implement our project
   
 ![vbes](https://user-images.githubusercontent.com/53348962/113097963-716efe00-9215-11eb-9b52-66f7b80d29d8.jpg)
 
   Level-2 Data Flow Diagram of our system
   
 ![vbes1](https://user-images.githubusercontent.com/53348962/113098177-c7dc3c80-9215-11eb-9222-2a6909770f91.jpg)
   
   Flow Chart
   
 ![main_flowChart-614x1024](https://user-images.githubusercontent.com/53348962/113098449-17226d00-9216-11eb-9907-8f87e20d8c88.jpg)

   Diagrams: Below are some important diagrams which explains the working and will be used in implementing the project.
   
 ![ER_Diagram_project-min-1024x692](https://user-images.githubusercontent.com/53348962/113098808-96b03c00-9216-11eb-89e0-37cbd083ac42.png)
