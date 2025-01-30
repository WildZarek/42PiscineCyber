# Piscine Discovery Cybersecurity

## Celulle00

This project is aimed to introduce us into the fascinating world of **Open Source Intelligence** (OSINT).

### Procedure

#### ex00

First, we are provided with this screenshot of a packet trace from Wireshack sniffer:

![Packet Trace from Wireshack](/.assets/img/packet_trace.png)

We need to found the social media used by that user, so let's do a basic search online.<br>
For usernames, I like to use the following website: [IDCrawl](https://www.idcrawl.com)

But, if you have Kali Linux or any Linux distribution focused to Cybersecurity,<br>
you could use a tool named **sherlock**. Choose what you prefer.
<br>

[[Search Results]](https://www.idcrawl.com/u/ihatetetris42)

![X Account of ihatetetris42](/.assets/img/x_ihatetetris42.png)

###### Example with Sherlock

![Sherlock Usage](/.assets/img/tyto00_sherlock.png)

#### ex01

Now, we are asked to found the real user account because this appears to be a fake profile.<br>
Easiest way is to check what accounts this user is following, which is only one. Let's take a look.

![Sherlock Usage](/.assets/img/ihatetetris42_follows.png)

After checking that profile, we found the real user behind the fake account.

![X Account of liam_up2u](/.assets/img/x_liam_up2u.png)

#### ex02

Continuing our investigation, we need to find geolocation of that user.<br>
First, we can search for any other social media accounts related to him (**liam_up2u**).
<br>
![IDCrawl for Liam](/.assets/img/liam_idcrawl.png)
[[Search Results]](https://www.idcrawl.com/u/liam_up2u)
<br>
![Liam's Instagram Profile](/.assets/img/liam_ig.png)
[[IG's liam]](https://www.instagram.com/liam_up2u/)

And if we go to this Instagram's profile, we can see just one photo uploaded.<br>
So, we can download that image and search by images at Google Images.

![Liam's Location](/.assets/img/liam_location.png)

> [!TIP]
> This technique is also know as **Imagery intelligence** ([IMINT](https://en.wikipedia.org/wiki/Imagery_intelligence)).

Finally, we got results pointing to **Argañín**, province of Zamora, at Castile and León (Spain).
<br>
[Result 1](https://es.wikipedia.org/wiki/Arga%C3%B1%C3%ADn) | [Result 2](https://pueblosdesayago.com/2020/10/25/la-iglesia-de-la-natividad-de-la-virgen-de-arganin/)

#### ex03

Our investigation is ending, but last, we are asked to find the phone model which that photo was taken.<br>
Time to explore through metadata! :mag_right:

For that pourpouse, you can use CLI tools like **Exiftool**, but I had prefer to use [fotoforensics.com](https://fotoforensics.com)
<br>
This website provide us with some useful data about an image, of course, metadata too.

![Image Metadata](/.assets/img/fotoforensics_tool.png)

## Celulle01

This project is aimed to introduce us into the fascinating world of **Web Exploitation** through common vulnerabilities.

### Procedure

#### ex00

We are provided with the following URL: [http://cybersec.42malaga.com:3317/](http://cybersec.42malaga.com:3317/)

![Web Exercise 00](/.assets/img/weasel00_web.png)

If we take a look at the link "HINT", we can see that are pointing to a file inside another folder.

Let's try if we can see more files inside that folder just removing the `hint.html` file from the URL.

![Web Exercise 00 Vulnerability](/.assets/img/weasel00_vuln.png)

As we can see, the web is vulnerable to Directory Listing due to a bad configuration of the HTTP server.

So entering the folder **flag/** we discover the `flag.txt` file with the solution to this exercise.

> [!TIP]
> In a real scenario, you could use a technique called **Fuzzing** to discover directories, files, subdomains and many more.
> We will see more about this in the next exercise.

###### Example of Fuzzing with wfuzz

![Fuzzing](/.assets/img/weasel00_result.png)

#### ex01

Next exercise seems solved in a similar maner, but this time we do not have any hint.

The URL is: [http://cybersec.42malaga.com:3318/](http://cybersec.42malaga.com:3318/)

![Web Exercise 01](/.assets/img/weasel01_web.png)

Let's apply what we learned in previous exercise, we can think about the same vulnerability,
so using the same technique we will use `wfuzz` to enumerate hidden directories.

![Fuzzing](/.assets/img/weasel01_result.png)

Go to the URL of that resource and check its content:

![Web Exercise 01 Vulnerability](/.assets/img/weasel01_vuln.png)

#### ex02

We are provided with another URL: [http://cybersec.42malaga.com:3319/](http://cybersec.42malaga.com:3319/)

This time, we see a little form where we can input the filename which we are looking for.

You could try to put `flag.txt` but in this case, we get this message:

![Web Exercise 02](/.assets/img/weasel02_msg.png)

Maybe the flag is in another directory, so we can think first in **Path Traversal Vulnerability**.

![Web Exercise 02 Vulnerability](/.assets/img/weasel02_vuln.png)

#### ex03

Finally, we have another URL: [http://cybersec.42malaga.com:3320/](http://cybersec.42malaga.com:3320/)

We can see a login form without any additional info. So first thing you can try is **SQL Injection Vulnerability**.

![Web Exercise 03 Vulnerability](/.assets/img/weasel02_vuln.png)

## Celulle02

This project is aimed to introduce us into the fascinating world of **Cryptography**.

### Procedure

#### ex00

In this first exercise we need to discover what algorithm was applied to the flag and we are hinted about using `Cyberchef`.

![Cryptography Exercise 00](/.assets/img/gecko00.png)

#### ex01

Similar exercise, but now we will learn about deciphering multiple algorithms and again, we are hinted about using `Cyberchef`.

![Cryptography Exercise 01](/.assets/img/gecko01.png)

#### ex02

In this case, we will learn about hashes and how to decrypt them. We are hinted about using `hashcat`.

> [!WARNING]  
> We do not have hashcat installed on the campus machines.
> 
> But that is not a problem because there is another way to solve this.

[CrackStation](https://crackstation.net/) is a website where you can try to crack most of the common hashes used.

So let's try if we have luck!

![Cryptography Exercise 02](/.assets/img/gecko02.png)

#### ex03

Last one. Now we have a little dictionary with words that could be part of the password.

We have the hash but we can't crack it without knowing the correct password to do that. Or maybe yes?

As seen in the subject of the exercise, we NEED to use `John The Ripper`.

Again, in my campus we don't have this tool, I could try to install it from Github or 

use some Linux distro focused on Cybersecurity, like Kali Linux.

First of all, I solved this because some others students give me the hint about a website called [hashes.com](https://hashes.com/en/decrypt/hash)

![Cryptography Exercise 03](/.assets/img/gecko03_result.png)

But to be honest, that is not the best way to solve this exercise because we SHOULD use the correct tool (as explained in the subject).

So I installed Kali Linux as a VM and this is result:

![Cryptography Exercise 03](/.assets/img/gecko03_john.png)

# Happy Hacking! ☠