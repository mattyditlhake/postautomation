# Video Poster Automation — TikTok, Facebook, YouTube

This project is a starter automation to upload videos to:
- TikTok (scaffold + instructions)
- Facebook (Page video upload implementation)
- YouTube (OAuth + resumable upload implementation)

IMPORTANT:
- TikTok API policies and endpoints change frequently. The included TikTok uploader is a scaffold with instructions and placeholders. You'll need to register for TikTok for Developers (or TikTok For Business) and follow their upload flow.
- For Facebook, you need a Page ID and Page Access Token with `pages_manage_posts` and `pages_read_engagement` permissions.
- For YouTube, you must enable YouTube Data API v3 and place `client_secrets.json` in project root.

Quick start:
1. Create a virtualenv and install requirements:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Edit `.env` and add credentials:
   - FACEBOOK_PAGE_ID, FACEBOOK_PAGE_ACCESS_TOKEN
   - TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET, TIKTOK_ACCESS_TOKEN (if available)
   - Place `client_secrets.json` for YouTube
3. Put videos in `videos/` and captions in `captions/`
4. Example upload:
   ```
   python main.py --platform facebook --video videos/test.mp4 --caption captions/test.txt
   ```
