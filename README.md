# Joindate Bot

Returns a CSV of all users in Discord server with their join date and time.

**To create a bot for your discord:**
1. Ensure you have admin permissions on the server you want to add your new bot to
2. Log in to discord website https://discord.com/
3. Go to Applications https://discord.com/developers/applications
4. Click "New Application"
5. Name your app, click "Create"
6. In sidebar, click "Bot" > "Add Bot" > "Yes, do it!"
7. Give your bot a username (can be same or different as the app name)
8. Copy the bot's TOKEN and put it in your ENV file as TOKEN
9. Go to "OAuth2" > "URL Generator"
10. Select "bot" in "SCOPES"
11. Give your bot the following permissions: (Admin - it will work with lesser perms, but if you're running this bot you're likely a server owner)
12. Copy the GENERATED URL and paste into your browser, this will invite your bot to the server you select
13. Check that your bot is in your server

### Run the code locally and it will save a spreadsheet with all users and join dates when it sees the message **"userdate".** If you have the same bot in multiple servers with the same TOKEN it will consolidate all users into one file.
