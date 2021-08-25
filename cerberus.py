import discord
import random
import os
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='+')
client.remove_command('help')


@client.event
async def on_message(message):

	if message.author == client.user:
		return
	
  #HELP
	if message.content == "+help":
		embed = discord.Embed(title="Help", description="Bot Commands (+)", color=discord.Colour.blue())
		embed.add_field(name="General Commands", value= f":star: `+ping - Latency Check`\n"
								f":star: `+8ball <question>- Ask Questions`\n" 
								f":star: `+how to hack - Get a list of useful resources`\n"
								f":star: `+owasp top 10 - OWASP TOP 10 Vulneabilities`\n")
		await message.channel.send(content=None, embed=embed)

	#How to Hack
	if message.content == "+how to hack":
		embed = discord.Embed(title="Get started with Hacking!", description=f"""Ethical Hacking is an authorized practice of bypassing system security to identify potential data breaches and threats in a network. The company that owns the system or network allows Cyber Security engineers to perform such activities in order to test the system’s defenses. Thus, unlike malicious hacking, this process is planned, approved, and more importantly, legal. Ethical hackers aim to investigate the system or network weak points that malicious hackers can exploit or destroy. They collect and analyze the information to figure out ways to strengthen the security of the system/network/applications. By doing so,  they can improve the security footprint so that it can better withstand attacks or divert them. Here are some useful resources.""", 
		color=discord.Colour.blue())

		embed.add_field(name="Youtube Channels", value="Hackersploit\n" "Liveoverflow\n" "John Hammond\n" "DC Cybersec\n" "Null Byte\n" "Pwn Function\n" "STOK\n" "The XSS Rat")

		embed.add_field(name="Certifications", value="CEH\n" "OSCP\n" "eCPPT\n" "Security+\n" "eJPT" )
		embed.add_field(name="Programming Languages", value="Python\n" "C, C++\n" "Ruby\n" "Javascript\n" "Go Lang\n")
		embed.add_field(name="Books", value="The Hackers Playbook Series\n" "The Web Application Hacker's Handbook\n" "Hacking the Art of Exploitation\n" "Web Hacking 101\n" "Penetration Testing: A Hands-on Introduction to Hacking\n")
		
		embed.add_field(name='Get Started', value="https://bit.ly/2Qvmmdg")
		embed.set_image(url='https://blog.hyperiondev.com/wp-content/uploads/2019/01/Blog-Hacker-Languages.jpg')
		await message.channel.send(content=None, embed=embed)

	#OWASP TOP 10
	if message.content == "+owasp top 10":
		embed = discord.Embed(title="OWASP TOP 10", description=("Owasp Top 10 is a list of top ten web application vulnerabilities"))
		embed.add_field(name="1. Injection", value="Injection flaws, such as SQL, NoSQ, OS, and LDAP injection, occur when untrusted data is sent to an interpreter as part of a command or query. The attacker’s hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.")
		embed.add_field(name="2. Broken Authentication", value="Application functions related to authentication and session management are often implemented incorrectly, allowing attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users’ identities temporarily or permanently.")
		embed.add_field(name="3. Sensitive Data Exposure", value="Many web applications and APIs do not properly protect sensitive data, such as financial, healthcare, and PII. Attackers may steal or modify such weakly protected data to conduct credit card fraud, identity theft, or other crimes. Sensitive data may be compromised without extra protection, such as encryption at rest or in transit, and requires special precautions when exchanged with the browser.")
		embed.add_field(name="4. XML External Entities (XXE)", value="Many older or poorly configured XML processors evaluate external entity references within XML documents. External entities can be used to disclose internal files using the file URI handler, internal file shares, internal port scanning, remote code execution, and denial of service attacks.")
		embed.add_field(name="5. Broken Access Control", value="Restrictions on what authenticated users are allowed to do are often not properly enforced. Attackers can exploit these flaws to access unauthorized functionality and/or data, such as access other users’ accounts, view sensitive files, modify other users’ data, change access rights, etc.")
		embed.add_field(name="6. Security Misconfiguration", value="Security misconfiguration is the most commonly seen issue. This is commonly a result of insecure default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages containing sensitive information. Not only must all operating systems, frameworks, libraries, and applications be securely configured, but they must be patched/upgraded in a timely fashion.")
		embed.add_field(name="7. Cross-Site Scripting (XSS)", value="XSS flaws occur whenever an application includes untrusted data in a new web page without proper validation or escaping, or updates an existing web page with user-supplied data using a browser API that can create HTML or JavaScript. XSS allows attackers to execute scripts in the victim’s browser which can hijack user sessions, deface web sites, or redirect the user to malicious sites.")
		embed.add_field(name="8. Insecure Deserialization", value="Insecure deserialization often leads to remote code execution. Even if deserialization flaws do not result in remote code execution, they can be used to perform attacks, including replay attacks, injection attacks, and privilege escalation attacks.")
		embed.add_field(name="9. Using Components with Known Vulnerabilities", value="Components, such as libraries, frameworks, and other software modules, run with the same privileges as the application. If a vulnerable component is exploited, such an attack can facilitate serious data loss or server takeover. Applications and APIs using components with known vulnerabilities may undermine application defenses and enable various attacks and impacts.")
		embed.add_field(name="10. Insufficient Logging & Monitoring", value="Insufficient logging and monitoring, coupled with missing or ineffective integration with incident response, allows attackers to further attack systems, maintain persistence, pivot to more systems, and tamper, extract, or destroy data. Most breach studies show time to detect a breach is over 200 days, typically detected by external parties rather than internal processes or monitoring.")
		await message.channel.send(content=None, embed=embed)
	else:
		await client.process_commands(message)

#PING
@client.command()
async def ping(ctx):
	await ctx.send(f"`Pong! {round(client.latency * 1000)}ms`")


#8ball
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	responses = ["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."
				]
	await ctx.send(f"**Question:** {question}\n**Answer:** {random.choice(responses)}")

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)