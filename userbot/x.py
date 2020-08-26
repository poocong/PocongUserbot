async def take_screen_shot(video_file: str, duration: int, path: str) -> str:
    """ take a screenshot """
    _LOG.info('[[[Extracting a frame from %s ||| Video duration => %s]]]', video_file, duration)
    ttl = duration // 2
    thumb_image_path = path or os.path.join(Config.DOWN_PATH, f"{basename(video_file)}.jpg")
    command = f"ffmpeg -ss {ttl} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        _LOG.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
