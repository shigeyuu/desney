import pandas as pd
import re
import datetime
import pytz
import time
import streamlit as st
import simpleaudio
def main():
    btn_flg = st.button('監視する')

    st.write('再販されたらお知らせします。')
    
    
    if btn_flg:
        while True:
            url = 'https://urtrip.jp/disneyland-sea-ticket-soldout/'
            data = pd.read_html(url, header = 0)
            df = data[1]
            search_date = '12-21'
            df['日付'] = df['日付'].apply(lambda x:x[:5])
            saihan = df[df['日付']==search_date].iloc[0,3][4:]
            split_saihan = re.split(':| |/', saihan)

            now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
            saihan_dt = datetime.datetime(now.year, int(split_saihan[0]),int(split_saihan[1]),int(split_saihan[2]),int(split_saihan[3]))
            now_dt = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)
            diff_dt = now_dt-saihan_dt
           

            if diff_dt.seconds/60<30:
                st.write(f'{search_date}分が再販されたので今すぐ購入してください。')
                link = '[<span class="hljs-string">Chemesim</span>](<span class="hljs-link">https://reserve.tokyodisneyresort.jp/ticket/search/?outside=1&route=2&parkTicketGroupCd=055&_gl=1*1djcy7p*_ga*MTE0ODQxODk4Ni4xNjY3NzAwMTAw*_ga_CW1JLMP4BH*MTY2NzcyMTg2NS4yLjEuMTY2NzcyMjAwMy41NS4wLjA.</span>)'
                st.markdown(link)
                while True:
                    wav_obj = simpleaudio.WaveObject.from_wave_file("可愛く輝く1.wav")
                    play_obj = wav_obj.play()
                    play_obj.wait_done()
                    
            print('まだ再販されていないようです。')
            time.sleep(60)
if __name__ == '__main__':
  main()
