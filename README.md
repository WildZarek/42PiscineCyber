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

![Web Exercise 01](/.assets/img/weasel00_web.png)

If we take a look at the link "HINT", we can see that are pointing to a file inside another folder.

Let's try if we can see more files inside that folder just removing the `hint.html` file from the URL.

![Web Exercise 01 Vulnerability](/.assets/img/weasel00_vuln.png)

As we can see, the web is vulnerable to Directory Listing due to a bad configuration of the http server.

So entering the folder **flag/** we discover the `flag.txt` file with the solution to this exercise.

> [!TIP]
> In a real scenario, you could use a technique called Fuzzing to discover directories, files, subdomains and many more.
> We will see more about this in the next exercise.

###### Example of Fuzzing with wfuzz

![Fuzzing](/.assets/img/weasel00_result.png)

#### ex01

#### ex02

#### ex03

## Celulle02

This project is aimed to introduce us into the fascinating world of **Cryptography**.

### Procedure

#### ex00

#### ex01

#### ex02

#### ex03