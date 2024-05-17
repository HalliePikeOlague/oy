import re
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize Colorama

def display_banner():
    banner_part1 = Fore.BLUE + """
88888888888                                888         888b     d888          d8b 888          
    888                                    888         8888b   d8888          Y8P 888          
    888                                    888         88888b.d88888              888          
    888   8888b.  888d888 .d88b.   .d88b.  888888      888Y88888P888  8888b.  888 888 .d8888b  
    888      "88b 888P"  d88P"88b d8P  Y8b 888         888 Y888P 888     "88b 888 888 88K      
    888  .d888888 888    888  888 88888888 888         888  Y8P  888 .d888888 888 888 "Y8888b. 
    888  888  888 888    Y88b 888 Y8b.     Y88b.       888   "   888 888  888 888 888      X88 
    888  "Y888888 888     "Y88888  "Y8888   "Y888      888       888 "Y888888 888 888  88888P' 
                              888                                                              
                         Y8b d88P                                                              
                          "Y88P"                                                               
           Extract Targeted Emails from Url's @rrustemHEKRI x @rrustemHEKRI_V2 
    """ + Style.RESET_ALL

    banner_part2 = Fore.MAGENTA + Style.BRIGHT + """
    For more tools and info about spamming, 
    join my Telegram channel: @rrustemHEKRI_V2

    For direct contact and inquiries, 
    reach out to the owner Telegram: @rrustemHEKRI
    """ + Style.RESET_ALL
    
    print(banner_part1 + banner_part2)

def extract_emails_from_lines(lines):
    emails = []
    for line in lines:
        # Using regex to split on '|', ';', or ':'
        parts = re.split(r'\||;|:', line.strip())
        if len(parts) > 1:  # Make sure there are enough parts
            email = parts[1]  # Assuming email is in the second part
            if '@' in email:
                emails.append(email)
                print(Fore.GREEN + "Extracted: " + Fore.MAGENTA + email + Style.RESET_ALL)  # Display each extracted email
    return emails

def display_thank_you():
    print(Fore.CYAN + "Thank you for using our Email Extractor.")
    print(Fore.CYAN + "For more great tools, check out our Telegram channel: " + Fore.RED + "@rrustemHEKRI_V2")
    print(Fore.CYAN + "Direct inquiries? Contact: " + Fore.RED + "@rrustemHEKRI")

def main():
    display_banner()

    # Ask the user for the file path
    file_path = input(Fore.GREEN + "Please enter the path to the URL file: ")
    
    # Ask the user for the domain to target
    target_domain = input(Fore.BLUE + "Please enter the target domain (e.g., 'grammarly.com'): ")
    output_file = f"{target_domain}-mails.txt"

    bookmarked_lines = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # First, bookmark lines that contain the targeted domain
            for line in file:
                if target_domain in line:
                    bookmarked_lines.append(line)

        # Now, extract emails from the bookmarked lines
        emails = extract_emails_from_lines(bookmarked_lines)

        # Save the emails to a file
        with open(output_file, 'w', encoding='utf-8') as f:
            for email in emails:
                f.write(email + '\n')

        if not emails:
            print(Fore.RED + "No emails found for the specified domain.")
        else:
            display_thank_you()

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    main()
