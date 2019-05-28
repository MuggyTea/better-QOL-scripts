#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytube import YouTube
import os
from pydub import AudioSegment
from logging_settings import logging_setting
import sys

logger = logging_setting('Log_youtube2wav')

def youtube2mp3(youtube_url):
    """ 
    youtubeのURLを入れるとwavファイルを返すスクリプト
    """
    logger.info('youtube url: {}'.format(youtube_url))
    print('youtube url: {}'.format(youtube_url))
    # S3にアップロード
    # upload_s3.sign_s3(youtube_url, 'youtube_url/{}'.format(youtube_url))
    # youtube動画を抜き出す
    yt = YouTube(youtube_url)
    # 動画の情報を出力
    for lis in yt.streams.all():
        logger.info(lis)
    # 保存先のディレクトリがなかったら作る
    if os.path.exists('youtube2mp4/') is not True:
        os.mkdir('youtube2mp4/')
    # 保存先のディレクトリがなかったら作る
    if os.path.exists('youtube2wav/') is not True:
        os.mkdir('youtube2wav/')
    # get_bu_itagtodownloadメソッドでビデオデータをダウンロードする
    yt2mp3 = yt.streams.get_by_itag(140).download('youtube2mp4/')
    # 空白を取り除く
    yt2mp3_re = yt2mp3.replace(' ', '')
    # 空白を取り除いたものにリネーム
    os.rename(yt2mp3, yt2mp3_re)
    logger.info('youtube video converted video/mp4 file name: {}'.format(yt2mp3_re))
    # 保存したmp4ファイルを呼び出す
    sound = AudioSegment.from_file(yt2mp3_re, "mp4")
    # 拡張子とファイル名をwavに書き換える
    yt2mp3_wav = yt2mp3_re.replace('mp4', 'wav')
    # wavにエクスポート
    sound.export(yt2mp3_wav, format="wav")
    # logger.info('rename: {}'.format(os.rename(yt2mp3, 'tmp/{}.mp4'.format(line_userid))))
    logger.info('Receive wav file name: {}'.format(yt2mp3_wav))
    # with open(yt2mp3, 'wb') as fb:
    #     fb.write(yt2mp3)

if __name__ == "__main__":
    # コマンドライン引数でURLを指定する
    youtube2mp3(sys.argv[1])
