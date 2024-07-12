import tkinter
import mutagen.mp3
import pygame
import requests
import tkinter.scrolledtext
import pathlib
import os
import time
import mutagen
from tkinter import filedialog, messagebox, ttk


class MusicPlayer(object):
    def __init__(self, window) -> None:
        self.window = window
        pygame.init()
        pygame.mixer.init()
        self.change_progress_task_id = None
        self.is_dragging = False
        self.ProgressIndex = 0


    def get_music(self):
        self.music_list = []
        self.music_path = pathlib.Path('D:\Music')
        self.mp3_file = self.music_path.glob('**/*.mp3')
        self.flac_file = self.music_path.glob('**/*.flac')
        for i in self.mp3_file:
            self.music_list.append(i)
        for i in self.flac_file:
            self.music_list.append(i)
        return self.music_list
            
        



    def init_ui(self):
        self.window.title('音乐播放器')
        self.window.geometry('685x500+1050+400')

        
        # 创建一个框架来包含Listbox和Scrollbar
        self.frame = tkinter.Frame(self.window)
        self.frame.pack(padx=10, pady=40)

        # 创建一个标签，名字为播放列表
        self.tile_text = tkinter.Label(self.window, text='播放列表', font=('SimHei', 15), width=10, height=1)
        self.tile_text.place(x=280, y=10)

        # 创建滚动条
        self.scrollbar = tkinter.Scrollbar(self.frame)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # 创建列表框
        self.playlist = tkinter.Listbox(self.frame, selectmode=tkinter.SINGLE, yscrollcommand=self.scrollbar.set, width=50, height=20)
        self.playlist.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.playlist.bind('<Double-1>', self.play)   #  绑定双击选择事件

        # 将滚动条与列表框关联
        self.scrollbar.config(command=self.playlist.yview)

        self.music_data = self.get_music()
        # 向列表框中添加数据
        for i in self.music_data:
            i = str(i).split('\\')[-1]
            self.playlist.insert(tkinter.END, i)

        # 播放/暂停
        self.play_status = tkinter.StringVar()
        self.play_status.set('▶')
        print(self.play_status)
        self.play_but = tkinter.Button(self.window, textvariable=self.play_status,  width=6, height=1, command=self.PauseOrUnpause)
        self.play_but.place(x=300, y=420)

         # 下一曲
        self.nextSong_but = tkinter.Button(self.window, text='⏭︎',  width=6, height=1, command=self.next_song)
        self.nextSong_but.place(x=450, y=420)


        # 上一曲
        self.PreviousSong_but = tkinter.Button(self.window, text='⏮',  width=6, height=1, command=self.revious_song)
        self.PreviousSong_but.place(x=150, y=420)


        # 音量控制
        self.volume_control = tkinter.Scale(self.window, from_=0, to=100, orient=tkinter.HORIZONTAL, command=self.set_vol)
        self.volume_control.set(50)
        self.volume_control.place(x=580, y=405)


        # 音量图标
        self.volume_label = tkinter.Label(self.window, text='🔊')
        self.volume_label.place(x=550, y=425)


                # 播放歌曲进度条
        self.progress = ttk.Scale(self.window, from_=0, to=100, orient=tkinter.HORIZONTAL)
        self.progress.pack(fill=tkinter.X, padx=15, pady=20)
        # 绑定拖动进度条事件
        self.progress.bind("<ButtonRelease-1>", self.on_progress_release)  # 释放拖拽


        
    def play(self, event):      # 双击选择音乐进行播放

        self.play_status.set('⏸')
        self.selection = self.playlist.curselection()
        if self.selection:
            self.Play_tracks = self.selection[0]
            print(self.music_list[self.Play_tracks])
            self.audio = mutagen.mp3.MP3(self.music_list[self.Play_tracks])
            self.audio_info = self.audio.info
            self.music_length = int(self.audio_info.length)
            if self.music_length > 60:
                self.music_length_m = int(self.music_length / 60)
                self.music_length_s = self.music_length % 60
                print(f'歌曲时长: {self.music_length_m}分{self.music_length_s}秒, 共{self.music_length}秒')
            else:
                print(f'歌曲时长: {int(self.music_length)}秒')
            pygame.mixer.music.load(self.music_list[self.Play_tracks])
            pygame.mixer.music.play()
            print('当前歌曲播放完毕, 开始检测下一曲是否能播放')
            self.check_music()
            
                    # 显示当前播放/歌曲总时长
        self.end_time_text = tkinter.StringVar()
        self.end_time_text.set(self.music_length)
        self.end_time_label = tkinter.Label(self.window, textvariable=self.end_time_text)
        self.end_time_label.place(x=645, y=445)


        self.temp_time_text = tkinter.StringVar()
        self.temp_time_text.set(self.music_length)
        self.temp_time_label = tkinter.Label(self.window, textvariable=self.end_time_text)
        self.temp_time_label.place(x=15, y=440)
        self.update_progress()
        






    def on_progress_release(self, event):

        # 获取滑动条的当前值
        self.new_position = self.progress.get()
        # 跳转到新的播放位置
        pygame.mixer.music.rewind()
        self.current_music_index = int(self.new_position) * self.music_length / 100
        pygame.mixer.music.set_pos(self.current_music_index)  # 转换毫秒到秒
        print(f'当前位置{int(self.new_position) * self.music_length / 100} / {self.music_length}')
        

    def update_progress(self):
        # 获取当前进度条的值
        current_value = self.progress.get()

        if current_value < self.music_length:
            self.progress.set(current_value + 0.1)

        else:
            self.progress.set(0)  # 或者停止更新，或者重置为0重新开始

        # 每1000毫秒（1秒）调用一次自身，更新进度条
        self.window.after(100, self.update_progress)  
        


    def check_music(self):    # 检查音乐是否播放完毕, 播放完毕后继续下一首
        #print('进入检测方法')
        if not pygame.mixer.music.get_busy():
            self.selection = list(self.selection)
            if self.Play_tracks >= len(self.music_list) - 1:
                self.Play_tracks = -1
            self.Play_tracks += 1
            print(f'当前歌曲{self.Play_tracks},{self.music_list[self.Play_tracks]}, 歌单共有{len(self.music_list)}')        
            pygame.mixer.music.load(self.music_list[self.Play_tracks])
            pygame.mixer.music.play()
            self.play_status.set('⏸')
            #print('开始检测')  # 每1000毫秒检测一次
        self.task_id = self.window.after(1000, self.check_music)

            #print('检测完毕')


        
    def stop_chick(self):
        if self.task_id:
            self.window.after_cancel(self.task_id)
            self.task_id = None


    def PauseOrUnpause(self):
        if pygame.mixer.music.get_busy():               # 检查是否正在播放
            self.play_status.set('▶')
            pygame.mixer.music.pause()
            self.stop_chick()

        else:
            self.play_status.set('⏸')
            pygame.mixer.music.unpause()
            self.check_music()


    def set_vol(self, num):
        num = float(num)/100
        pygame.mixer.music.set_volume(num)


    def next_song(self):
        self.play_status.set('⏸')
        self.selection = list(self.selection)
        if self.Play_tracks >= len(self.music_list) - 1:
            self.Play_tracks = -1
        self.Play_tracks += 1
        print(f'当前歌曲{self.Play_tracks},{self.music_list[self.Play_tracks]}, 歌单共有{len(self.music_list)}')        
        pygame.mixer.music.load(self.music_list[self.Play_tracks])
        pygame.mixer.music.play()

    
    def revious_song(self):
        self.play_status.set('⏸')
        self.selection = list(self.selection)
        if self.Play_tracks <= 0:
            self.Play_tracks = len(self.music_list)
        self.Play_tracks -= 1
        print(self.Play_tracks)        
        pygame.mixer.music.load(self.music_list[self.Play_tracks])
        pygame.mixer.music.play()




def RunMusicPlayer() -> None:
    window = tkinter.Tk()
    ZMJ_CALA = MusicPlayer(window)
    ZMJ_CALA.init_ui()
    window.mainloop()

RunMusicPlayer()
