import random
import streamlit as st

questions = [
    "What is the difference between a hub, switch, and router?",
    "What are the characteristics of TCP and UDP?",
    "What is SIEM, and what is its purpose?",
    "Define EDR and XDR in cybersecurity.",
    "Explain the difference between Simplex, Half-Duplex, and Full-Duplex communication.",
    "What are the three pillars of the CIA triad in cybersecurity?",
    "What is the difference between symmetric and asymmetric encryption?",
    "What are the private IP address ranges for Class A, B, and C?",
    "What is NAT, and how does it work?",
    "What are the different types of hackers, such as White Hat, Black Hat, and Grey Hat?",
    "What is a MAC address, and how does ARP work?",
    "Explain the difference between Surface Web, Deep Web, and Dark Web.",
    "How does DNS work, and what are the roles of DNS root servers?",
    "What is the DHCP DORA process?",
    "Explain the purpose of HTTP, FTP, SMTP, and SSH protocols.",
    "What is the difference between Authorization, Authentication, and Accounting (AAA)?",
    "What do MBps and Mbps stand for, and where are they used?",
    "What is the role of Active Directory (AD) in a network?",
    "Explain the difference between NTLM and Kerberos authentication protocols.",
    "What is a packet, and how does packet transmission work?",
    "What is the OSI model, and what are its seven layers?",
    "What is the difference between Indicators of Compromise (IOC) and Indicators of Attack (IOA)?",
    "What is a proxy server, and how does it enhance privacy?",
    "What is the role of a firewall, and how does a load balancer work?",
    "What tools are used to check IP, domain, hash, and URL reputations?",
    "What are DNS records, and what are the different types like A, AAAA, MX, and CNAME?",
    "What is a SIEM system, and what are some examples of SIEM tools?",
    "What is EDR, and how does it help with endpoint protection?",
    "What is Syslog, and what is its role in log collection?",
    "Define vulnerability, threat, risk, and exploit in the context of cybersecurity.",
    "What are the different types of malware, such as viruses, worms, and ransomware?",
    "What is the Cyber Kill Chain, and what are its stages?",
    "Explain the difference between horizontal and vertical port scanning.",
    "What is a DoS attack, and how does it differ from a DDoS or DRDoS attack?",
    "What is the Mirai Botnet, and how does it perform DDoS attacks?",
    "What is a brute force attack, and what are some common types like dictionary and rainbow table attacks?",
    "What steps can be taken to mitigate brute force attacks?",
    "What is an SQL injection attack, and how can it be prevented?",
    "What happens when an SQL injection query contains 'OR 1=1'?",
    "What are the key methods of system hardening?",
    "What is the Defense in Depth strategy?",
    "Explain the difference between an in-house SOC and an MSSP SOC.",
    "What is a hybrid SOC?",
    "What is the Zero Trust Model, and why is it important in cybersecurity?",
    "What is a Zero-Day attack?",
    "What is ARP protocol impersonation, and how does it work?",
    "What is eavesdropping in cybersecurity?",
    "What is packet sniffing, and how is it used in network monitoring?",
    "What is the MITRE ATT&CK framework, and how is it useful in cybersecurity?",
    "What is DNS spoofing, and how does it redirect traffic to a fake site?"
]


class AskQuestion:
    def __init__(self, question_list):
        self.remaining_questions = question_list.copy()
        self.asked_questions = []

    def pick_question(self):
        if not self.remaining_questions: 
            self.remaining_questions = self.asked_questions.copy()
            self.asked_questions.clear()
        question = random.choice(self.remaining_questions)
        self.remaining_questions.remove(question)
        self.asked_questions.append(question)
        return question


if 'question_instance' not in st.session_state:
    st.session_state.question_instance = AskQuestion(questions)

if 'last_question' not in st.session_state:
    st.session_state.last_question = None

if st.button('Get a New Question'):
    st.session_state.last_question = st.session_state.question_instance.pick_question()

if st.session_state.last_question:
    st.write(st.session_state.last_question)
else:
    st.write("Press the button to get a question!")