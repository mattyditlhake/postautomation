#!/usr/bin/env python3
"""Main entrypoint: upload to facebook, youtube, or tiktok"""
import argparse, logging
from dotenv import load_dotenv
from uploaders.facebook_uploader import FacebookUploader
from uploaders.youtube_uploader import YouTubeUploader
from uploaders.tiktok_uploader import TikTokUploader
from utils.file_loader import load_caption
import os

load_dotenv()
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

UPLOADERS = {
    'facebook': FacebookUploader,
    'youtube': YouTubeUploader,
    'tiktok': TikTokUploader,
}

def run_upload(platform, video_path, caption_text, title=None, dry_run=False):
    uploader_cls = UPLOADERS.get(platform)
    if not uploader_cls:
        logger.error('Unsupported platform: %s', platform)
        return False
    uploader = uploader_cls()
    if dry_run:
        logger.info('Dry run: would upload %s to %s with caption: %s', video_path, platform, caption_text)
        return True
    success, meta = uploader.upload(video_path, caption_text, title=title)
    if success:
        logger.info('Upload succeeded: %s', meta.get('url') or meta.get('id') or str(meta)[:200])
    else:
        logger.error('Upload failed: %s', meta)
    return success

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--platform', required=True, choices=list(UPLOADERS.keys()))
    parser.add_argument('--video', required=True)
    parser.add_argument('--caption', required=False)
    parser.add_argument('--caption-text', required=False)
    parser.add_argument('--title', required=False)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    caption_text = args.caption_text
    if args.caption and not caption_text:
        caption_text = load_caption(args.caption)
    if caption_text is None:
        caption_text = ''
    run_upload(args.platform, args.video, caption_text, title=args.title, dry_run=args.dry_run)

if __name__ == '__main__':
    main()
