import subprocess
import sys
import os
import glob
import urllib.request
from urllib.parse import quote

# List of applications to remove
apps_to_remove = [
	"2048-qt",
	"gnome-weather",
	"gnome-maps",
	"aisleriot",
	"atril",
	"cheese",
	"gnome-chess",
	"evolution",
	"gnome-klotski",
	"libreoffice*",
	"gnome-mahjongg",
	"gnome-mines",
	"gnome-nibbles",
	"spooftooph",
	"gnome-taquin",
	"impacket-scripts",
	"onesixtyone",
	"ophcrack-cli",
	"gnome-2048",
	"gnome-contacts",
	"five-or-more",
	"four-in-a-row",
	"gtkhash",
	"thunar-gtkhash",
	"hitori",
	"tali",
	"gnome-sudoku",
	"swell-foop",
	"quadrapassel",
	"autopsy",
	"bulk-extractor",
	"cryptsetup",
	"exe2hexbat",
	"sleuthkit",
	"dns2tcp",
	"dns2tcpc",
	"faraday",
	"faraday-cli",
	"lbd",
	"gnome-tetravex",
	"sqlmap", 
	"cutycapt",
	"evil-winrm",
	"mimikatz",
	"nikto",
	"aircrack-ng",
	"amass",
	"arping",
	"binwalk",
	"bully",
	"burpsuite",
	"cadaver",
	"cewl",
	"cherrytree",
	"chntpw",
	"clang",
	"commix",
	"crackmapexec",
	"crunch",
	"davtest",
	"dbd",
	"dirb",
	"dirbuster",
	"dmitry",
	"dnschef",
	"dnsenum",
	"dnsrecon",
	"enum4linux",
	"ettercap-graphical",
	"fern wifi cracker",
	"ffuf",
	"fierce",
	"fping",
	"ghidra",
	"guymager",
	"hash-identifier",
	"hashcat",
	"hashdeep",
	"hashid",
	"hping3",
	"hydra",
	"ike-scan",
	"iodine",
	"john",
	"kismet",
	"laudanum",
	"legion (root)",
	"macchanger",
	"magicrescue",
	"masscan",
	"medusa",
	"minicom",
	"miredo",
	"mitmproxy",
	"msf payload creator",
	"NASM shell",
	"nbtscan",
	"ncrack",
	"netdiscover",
	"netmask",
	"netsniff-ng",
	"nmap",
	"ollydbg",
	"patator",
	"pdf-parser",
	"pdfid",
	"pipal",
	"pixiewps",
	"powershell empire",
	"proxychains4",
	"proxytunnel",
	"ptunnel",
	"pwnat",
	"radare2",
	"reaver",
	"rebind",
	"recon-ng",
	"recordmydesktop",
	"responder",
	"rsmangler",
	"samdump2",
	"sbd",
	"scalpel",
	"scrounge-ntfs",
	"skipfish",
	"smbmap",
	"smpmap",
	"social engineering toolkit",
	"spiderfoot",
	"spike",
	"ssldump",
	"sslg",
	"sslh",
	"sslscan",
	"sslsplit",
	"sslyze",
	"starkiller",
	"stunnel4",
	"swaks",
	"tcpdump",
	"tcpreplay",
	"thc-pptp-bruter",
	"theharvester",
	"udptunnel",
	"voiphopper",
	"wafw00f",
	"wapiti",
	"webshells",
	"weevely",
	"wfuzz",
	"whatweb",
	"wifite",
	"wireshark",
	"wordlists"
]

files_to_remove = [
	"/usr/share/applications/kali*",
	"/usr/share/applications/sqlitebrowser.desktop.disabled-by-kali-menu",
	"/usr/share/applications/sqlitebrowser.destkop",
	"/usr/share/applications/exploit-database.desktop",
	"/usr/share/applications/kali-pth-smbget.desktop",
	"/usr/share/applications/kali-pth-curl.desktop",
	"/usr/share/applications/kali-pth-net.desktop",
	"/usr/share/applications/kali-pth-rpcclient.desktop",
	"/usr/share/applications/kali-pth-sqsh.desktop",
	"/usr/share/applications/kali-pth-winexe.desktop",
	"/usr/share/applications/kali-pth-wmic.desktop",
	"/usr/share/applications/kali-pth-wmis.desktop",
	"/usr/share/applications/kali-bugs.desktop",
	"/usr/share/applications/kali-docs.desktop",
	"/usr/share/applications/kali-forums.desktop",
	"/usr/share/applications/kali-maltego-installer.desktop",
	"/usr/share/applications/kali-netcat.desktop",
	"/usr/share/applications/kali-nethunter.desktop",
	"/usr/share/applications/kali-onesixtyone.desktop",
	"/usr/share/applications/kali-ophcrack-cli.desktop",
	"/usr/share/applications/kali-powersploit.desktop",
	"/usr/share/applications/kali-pth-smbclient.desktop",
	"/usr/share/applications/kali-pwsh.desktop",
	"/usr/share/applications/kali-scapy.desktop",
	"/usr/share/applications/kali-searchsploit.desktop",
	"/usr/share/applications/kali-snmpcheck.desktop",
	"/usr/share/applications/kali-spooftooph.desktop",
	"/usr/share/applications/kali-thcping6.desktop",
	"/usr/share/applications/kali-tools.desktop",
	"/usr/share/applications/kali-unix-privesc-check.desktop",
	"/usr/share/applications/kali-www.desktop",
	"/usr/share/applications/offsec-training.desktop",
	"/usr/share/applications/onboard-settings.desktop",
	"/usr/share/applications/onboard.desktop",
	"/usr/share/applications/ophcrack.desktop",
	"/usr/share/applications/sqlitebrowser.desktop",
	"/usr/share/applicatons/kali-pth-smbclient.desktop",
	"/usr/share/desktop-directories/002-protect.directory",
	"/usr/share/desktop-directories/003-detect.directory",
	"/usr/share/desktop-directories/004-respond.directory",
	"/usr/share/desktop-directories/005-recover.directory",
	"/usr/share/desktop-directories/01-01-dns-analysis.directory",
	"/usr/share/desktop-directories/01-02-identify-live-hosts.directory",
	"/usr/share/desktop-directories/01-03-ids-ips-identification.directory",
	"/usr/share/desktop-directories/01-04-network-scanners.directory",
	"/usr/share/desktop-directories/01-07-osint-analysis.directory",
	"/usr/share/desktop-directories/01-08-route-analysis.directory",
	"/usr/share/desktop-directories/01-10-smb-analysis.directory",
	"/usr/share/desktop-directories/01-11-smtp-analysis.directory",
	"/usr/share/desktop-directories/01-12-snmp-analysis.directory",
	"/usr/share/desktop-directories/01-13-ssl-analysis.directory",
	"/usr/share/desktop-directories/01-info-gathering.directory",
	"/usr/share/desktop-directories/02-01-cisco-tools.directory",
	"/usr/share/desktop-directories/02-02-fuzzers.directory",
	"/usr/share/desktop-directories/02-03-voip-tools.directory",
	"/usr/share/desktop-directories/02-05-nessus.directory",
	"/usr/share/desktop-directories/02-06-openvas.directory",
	"/usr/share/desktop-directories/02-07-stress-testing.directory",
	"/usr/share/desktop-directories/02-08-gvm.directory",
	"/usr/share/desktop-directories/02-vulnerability-analysis.directory",
	"/usr/share/desktop-directories/03-01-cms-identification.directory",
	"/usr/share/desktop-directories/03-04-web-crawlers.directory",
	"/usr/share/desktop-directories/03-05-web-vulnerability-scanners.directory",
	"/usr/share/desktop-directories/03-06-web-application-proxies.directory",
	"/usr/share/desktop-directories/03-webapp-analysis.directory",
	"/usr/share/desktop-directories/04-database-assessment.directory",
	"/usr/share/desktop-directories/05-01-online-attacks.directory",
	"/usr/share/desktop-directories/05-02-offline-attacks.directory",
	"/usr/share/desktop-directories/05-04-pass-hash.directory",
	"/usr/share/desktop-directories/05-05-profile.directory",
	"/usr/share/desktop-directories/05-password-attacks.directory",
	"/usr/share/desktop-directories/06-01-wireless-tools.directory",
	"/usr/share/desktop-directories/06-02-bluetooth-tools.directory",
	"/usr/share/desktop-directories/06-03-rfid-nfc-tools.directory",
	"/usr/share/desktop-directories/06-04-other-wireless.directory",
	"/usr/share/desktop-directories/06-05-radio-tools.directory",
	"/usr/share/desktop-directories/06-wireless-attacks.directory",
	"/usr/share/desktop-directories/07-reverseengineer.directory",
	"/usr/share/desktop-directories/08-01-metasploit-framework.directory",
	"/usr/share/desktop-directories/08-exploitation-tools.directory",
	"/usr/share/desktop-directories/09-01-network-sniffers.directory",
	"/usr/share/desktop-directories/09-02-network-spoofing.directory",
	"/usr/share/desktop-directories/09-sniffing-spoofing.directory",
	"/usr/share/desktop-directories/10-01-os-backdoors.directory",
	"/usr/share/desktop-directories/10-02-tunneling.directory",
	"/usr/share/desktop-directories/10-03-web-backdoors.directory",
	"/usr/share/desktop-directories/10-04-command-control.directory",
	"/usr/share/desktop-directories/10-maintaining-access.directory",
	"/usr/share/desktop-directories/11-01-network-forensics.directory",
	"/usr/share/desktop-directories/11-03-digital-forensics.directory",
	"/usr/share/desktop-directories/11-04-forensic-analysis-tools.directory",
	"/usr/share/desktop-directories/11-05-forensic-carving-tools.directory",
	"/usr/share/desktop-directories/11-07-forensic-imaging-tools.directory",
	"/usr/share/desktop-directories/11-08-forensic-suites.directory",
	"/usr/share/desktop-directories/11-11-pdf-forensics-tools.directory",
	"/usr/share/desktop-directories/11-forensics.directory",
	"/usr/share/desktop-directories/12-reporting.directory",
	"/usr/share/desktop-directories/13-social-engineering-tools.directory",
	"/usr/share/desktop-directories/14-01-gpsd-service.directory",
	"/usr/share/desktop-directories/14-02-httpd-service.directory",
	"/usr/share/desktop-directories/14-03-mysqld-service.directory",
	"/usr/share/desktop-directories/14-04-pcscd-service.directory",
	"/usr/share/desktop-directories/14-06-sshd-service.directory",
	"/usr/share/desktop-directories/14-07-radius-service.directory",
	"/usr/share/desktop-directories/14-08-beef-service.directory",
	"/usr/share/desktop-directories/14-09-metasploit-service.directory",
	"/usr/share/desktop-directories/14-10-dradis-service.directory",
	"/usr/share/desktop-directories/14-11-openvas-service.directory",
	"/usr/share/desktop-directories/14-12-xplico-service.directory",
	"/usr/share/desktop-directories/14-13-gvm-service.directory",
	"/usr/share/desktop-directories/14-14-faraday-service.directory",
	"/usr/share/desktop-directories/14-15-nessus-service.directory",
	"/usr/share/desktop-directories/14-16-defectdojo-service.directory",
	"/usr/share/desktop-directories/14-services.directory",
	"/usr/share/desktop-directories/15-kali-offsec-links.directory",
    "/usr/share/applications/exploit-database.desktop",
    "/usr/share/applications/kali-maltego-installer.desktop",
    "/usr/share/applications/vulnhub.desktop",
    "/usr/share/desktop-directories/001-identify.directory",
]

def remove_app(app):
    try:
        print(f"Attempting to remove {app}...")
        subprocess.run(["sudo", "apt-get", "remove", "-y", app], check=True)
        print(f"Removed {app} successfully.\n")
    except subprocess.CalledProcessError:
        print(f"Failed to remove {app}. It might not be installed.\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}\n")

def remove_files(paths):
    for path in paths:
        try:
            matched_files = glob.glob(path)
            if not matched_files:
                print(f"No files matched: {path}")
                continue

            for file in matched_files:
                os.remove(file)
                print(f"Removed: {file}")
        except PermissionError:
            print(f"Permission denied: Cannot remove {path}. Try running the script with sudo.")
        except Exception as e:
            print(f"An error occurred while trying to remove {path}: {str(e)}")

remove_files(files_to_remove)
for app in apps_to_remove:
    remove_app(app)
try:
    subprocess.run(["sudo", "apt-get", "autoremove", "-y"], check=True)
    print("Autoremove completed successfully.")
except subprocess.CalledProcessError:
    print("Autoremove failed.")
except Exception as e:
    print(f"An error occurred during autoremove: {str(e)}")