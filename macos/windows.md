# Running Windows 10 on macOS

A [Twine issue](https://github.com/pypa/twine/issues/671) prompted me to go down this rabbit hole, in the interest of supporting the large number of folks who _aren't_ using macOS or Linux.

I'm currently using a virtual machine (VM) created from an ISO using the Parallels Desktop trial. I'm suprisingly happy with the arrangement, although I haven't used it much beyond running some Python code. I'd like try using it for Python development, and maybe gaming (since [macOS no longer supports some older games](https://support.steampowered.com/kb_article.php?ref=1055-ISJM-8568)).

I didn't try [Boot Camp](https://support.apple.com/boot-camp), partly due to disk space and the complexities of dual-booting in general, but also because it seems that [Apple’s new processors won’t support Windows through Boot Camp](https://www.theverge.com/2020/6/24/21302213/apple-silicon-mac-arm-windows-support-boot-camp).

VMs can take up a lot of disk space, so I tried using them from an external hard disk drive (HDD), but that was very slow. For now, I freed up a bunch of space on my iMac's internal SSD, and will just keep an eye on the size. I might try an external SSD someday.

## Getting Windows

### [Disc image (ISO File)](https://www.microsoft.com/en-us/software-download/windows10ISO)

- Technically requires buying a license, but it seems usable without one
- 5 GB download, 16 GB installed
- Need to create VM manually

### [Windows 10 developer virtual machines](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

- Includes Visual Studio, VS Code, WSL, Ubuntu, Windows terminal,...
- Free to use, with expiration date
- Pre-packaged VMs for Parallels, VMware, etc. makes it easy to start using
- 18 GB zip download, 50 GB installed
- Nice to have all the things installed, but you might not need them
- Not representative of a "normal" Windows user's experience

### [Microsoft Edge developer virtual machines](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)

- Windows 10 with Legacy Microsoft Edge and Internet Explorer 11
- Free, with 90 day expiration
- 7 GB zip
- Haven't tried this in awhile, might be limited

## Virtualization Software

### [Parallels Desktop](https://www.parallels.com/products/desktop/)

- $79.99+ after free trial
- Automated install from ISO
- Fast to boot and use
- Switching between windowed and full-screen mode "just works"
- Turned off lots of "helpful" features that I don't care about
    - Shared applications and files
    - Keyboard shortcuts (e.g. don't use "command" as "ctrl")
- Looks promising for games with lower system requirements (e.g. Portal 2)

### [VMware Fusion](https://www.vmware.com/products/fusion.html)

Looking forward to [VMware Fusion 12 Player](https://blogs.vmware.com/teamfusion/2020/08/announcing-fusion-12-and-workstation-16.html):

- Free for personal use
- DirectX 11 support
- Released by end of October
- [Tech Preview available for download](https://blogs.vmware.com/teamfusion/tech-preview)

### [VirtualBox](https://www.virtualbox.org/)

Free to use, but...

This is just not usable for me, regardless of whether I installed from a pre-packaged VM or from scratch. It's very slow to boot, sluggish to use, and it was hard to figure out the display size/resolution due to the iMac Retina display.

Also, installing from the ISO was a completely manual process, involving lots of interaction with Cortana. 👎
