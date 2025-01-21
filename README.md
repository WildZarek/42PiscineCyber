# Piscine Discovery Ciberseguridad

## Celulle00

This project is aimed to introduce us into the fascinating world of **Open Source Intelligence** (OSINT).

### Procedure

#### ex00

First, we are provided with this screenshot of a packet trace from Wireshack sniffer:

![Packet Trace from Wireshack](/.assets/packet_trace.png)

We need to found the social media used by that user, so let's do a basic search online.<br>
For usernames, I like to use the following website: [IDCrawl](https://www.idcrawl.com)

But, if you have Kali Linux or any Linux distribution focused to Cybersecurity,<br>
you could use a tool named **sherlock**. Choose what you prefer.
<br>
[[Search Results]](https://www.idcrawl.com/u/ihatetetris42)

<!-- link to image for X reference -->

#### ex01

Now, we are asked to found the real user account because this appears to be a fake profile.<br>
Easiest way is to check what accounts this user is following, which is only one. Let's take a look.

<!-- insert image to following users -->

After checking that profile, we found the real user behind the fake account.

<!-- inser image to header of X account -->

#### ex02

Continuing our investigation, we need to find geolocation of that user.<br>
First, we can search for any other social media accounts related to him (**liam_up2u**).
<br>
![IDCrawl for Liam](/.assets/liam_idcrawl.png)
[[Search Results]](https://www.idcrawl.com/u/liam_up2u)
<br>
![Liam's Instagram Profile](/.assets/liam_ig.png)
[[IG's liam]](https://www.instagram.com/liam_up2u/)

And if we go to this Instagram's profile, we can see just one photo uploaded.<br>
So, we can download that image and search by images at Google Images.

![Liam's Location](/.assets/liam_location.png)

> [!TIP]
> This technique is also know as **Imagery intelligence** ([IMINT](https://en.wikipedia.org/wiki/Imagery_intelligence)).

Finally, we got results pointing to **Argañín**, province of Zamora, at Castile and León (Spain).

[Result 1](https://es.wikipedia.org/wiki/Arga%C3%B1%C3%ADn) | [Result 2](https://pueblosdesayago.com/2020/10/25/la-iglesia-de-la-natividad-de-la-virgen-de-arganin/)

#### ex03

Our investigation is ending, but last, we are asked to find the phone model which that photo was taken.<br>
Time to explore through metadata! :mag_right:

For that pourpouse, you can use CLI tools like **Exiftool**, but I had prefer to use [fotoforensics.com](https://fotoforensics.com)
<br>
This website provide us with some useful data about an image, of course, metadata too.

![Image Metadata](/.assets/fotoforensics_tool.png)

