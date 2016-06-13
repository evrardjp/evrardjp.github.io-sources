Title:  My YubiKey Quickstart guide
Date: 2016-06-12 22:30
Category: security
Tags: yubikey, pgp, ssh
Summary: Securing my world by using YubiKeysHere is how I use YubiKeys

![yubikey-photo](https://farm3.staticflickr.com/2625/3689896409_35043dc8ba_d.jpg)

It's been a while that I'm thinking to step into the smart card world. It's been years that I've got a smart card on me all the time, but I only use it once a year.
For paying my taxes. Everytime I use it, I'm complaining. A lot.

Here are a few reasons for it:

1. everything linked to its usage as a smart card is poorly documented. I really hope it's not by design.
1. it requires specific hardware: a special kind of smart card reader (so not every smart card reader works!)
1. it requires specific software: a specific version of java (YMMV when using the latest version on java64!), and sometimes even your version of java32 doesn't work with it
1. it doesn't work on all the browsers! You need to have a specific plugin. Of course, if you insert your smart card **AFTER** launching Firefox, you're good for its restart.
1. you can't do whatever you want with it (can't set your own keys ...)

Taxes feeling + grumpy {soft,hard}ware makes me unhappy, and I am unlikely to use it in other circumstances.

So, I decided to give YubiKeys a go.

# What are YubiKeys, and why would I want one?

Recently I found the YubiKeys more interesting:

- The YubiKey 4 doesn't cost much for this whole list of features and...
- There is a 20% discount for github users on yubico website ("temporary offer")
- The YubiKey works as HID for **2**-**F**actor **A**uthentication mechanisms (fido u2fa, yubico OTP, ...) and ...
- It also works for CCID (smart cards! you can use it for pgp, ssh, or for many other purposes)
- It only needs a good ol' USB port to work.
- The YubiKey Neo adds NFC to the mix for your mobile (but have drawnbacks, check the cypto specs here <https://www.yubico.com/products/yubikey-hardware/>). FYI, the neo is currently cheaper on amazon than it is on yubico website.

# Ok I'm in! Where should I start ?

Simple question, long answer. Don't start with the "documentation" of the [dev.yubico][] website.
There is so much documentation on their website, you'll be lost in all the links.

Here is what I'd do:

1. Simply start on your device page ([yubikey 4][]/[yubikey neo][]) and absorb what's there.
1. You should then find the [getting started page][yubico-start] interesting.
1. You should then go ahead with the [personalisation tools page][yubico-pt-page].

You have plenty links on these three pages to follow what's really needed to your use case. The last page would obviously link to a download for the [yubico personalisation tool][yubico-pt]. This tool makes possible in-depth changes of your YubiKey.

# Any other links?

For github/google, go to your security settings. U2FA is really simple and doesn't need much explanation. You shouldn't need any other link or personalisation tool for it. For non-U2FA, that's where the fun begins...

Here are a few interesting explanations I found by browsing the interwebz/yubico website:

- [Configuring Yubikey as generic OATH HOTP token generator][generic-hotp]. It could be useful on Ubuntu One, but I didn't see the option there.
- [Configuring YubiKey as a smartcard for ssh authentication, CA or code signing][ssh-cert]. Starting from openssh-5.4p1 it should be simple to use PKCS#11. On this page, you should look for the SSH with PIV and PKCS#11 section. Check also [here][piv-slots] for the explanation of the PIV slots.
- Configuring PAM and SSH server for a 2FA with Yubico OTP ([1][] [2][] [3][] [4][] ). Take these with a pinch of salt (Some pages claim to improve security by using their method, where it clearly doesn't. More on that in a later article).
- [Configuring PGP with YubiKeys][pgp]

[dev.yubico]: https://developers.yubico.com/
[yubikey 4]: http://yubi.co/4
[yubikey neo]: http://yubi.co/neo
[yubico-start]: https://www.yubico.com/start/
[yubico-pt]: https://www.yubico.com/pt
[yubico-pt-page]: https://www.yubico.com/products/services-software/personalization-tools/
[generic-hotp]: https://www.yubico.com/products/services-software/personalization-tools/oath/
[ssh-cert]: https://www.yubico.com/why-yubico/for-individuals/computer-login/yubikey-neo-and-piv/
[piv-slots]: https://developers.yubico.com/PIV/Introduction/Certificate_slots.html
[1]: https://derekriemer.com/node/25
[2]: http://delyan.me/securing-ssh-with-totp/
[3]: https://www.100tb.com/blog/ssh-two-factor-authentication-with-totp-in-debianubuntu/
[4]: http://strugglers.net/~andy/blog/2016/05/06/using-a-totp-app-for-multi-factor-ssh-auth/
[pgp]: https://developers.yubico.com/PGP/

*Photo credit: [Thomas Flenstad](https://www.flickr.com/photos/11506685@N07/3689896409/)*