import requests
import json
import ClientMain
import time 
from bs4 import BeautifulSoup



class GmTools(object):
      
      def __init__(self) -> None:
            self.cooks = {
      'gdf_gm_session': 'Nb3onAy1HtTu66YGUIxh3UutpOBfYmj00T6J6K00o83%2Fyn%2B3NTPiyztdLXV1kmAuA%2F%2BlaPwlIedC5jsel1iJ1VjgLGFpVDoD8WyQuI8rVWaGY0SuZwBzprEvaGQVbtuy6gDq1V9p6pP5s5DfTTqLrMQSQdAsfouMkTuKx4YCwQSTyCQOZzBzij7hnPjVvt9GPUH6X6mq9pZE3sVKs62wneC%2FjYVFucHx1G50dJILEy51iqRtoXSPWwHOgCmDxgdS0w8oIT%2By6lNEe%2FNuJCU7sHgmjZCiwsrEcGkGiAPVOMH1xZHvGMASUx3g%2Bx5Aw7v%2Bn0viWTBN6x0GWRCHv5jdJtaSPbHw3Ym4n2XJtv2UT8hHwxakiplrRaZNxy2DNB7s192ptG9DUKI4bmlVVodLJ%2F2GrdxrKQ8MncMI0qJPExNrRrfUIWc6t7uSvOrpBO4SDUvya%2FAw77T5l6403TXsUA3eBDQYy8%2FsYe66lGZ8hhHRb25c6efBREeth3Tgc2Z8LanyISfbkyTqeYznC0e2P7kZkXlEIBI%2BuzoKDvleIo3UrX%2BeOwRxw0PojS0FCWxRvmebw%2BiQWOqGw8x1Lb9tug%3D%3Db61311e1e7e83e618b7287ec23b49acf01b613d2',
      }
            self.headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
      # 'Cookie': 'gdf_gm_session=Nb3onAy1HtTu66YGUIxh3UutpOBfYmj00T6J6K00o83%2Fyn%2B3NTPiyztdLXV1kmAuA%2F%2BlaPwlIedC5jsel1iJ1VjgLGFpVDoD8WyQuI8rVWaGY0SuZwBzprEvaGQVbtuy6gDq1V9p6pP5s5DfTTqLrMQSQdAsfouMkTuKx4YCwQSTyCQOZzBzij7hnPjVvt9GPUH6X6mq9pZE3sVKs62wneC%2FjYVFucHx1G50dJILEy51iqRtoXSPWwHOgCmDxgdS0w8oIT%2By6lNEe%2FNuJCU7sHgmjZCiwsrEcGkGiAPVOMH1xZHvGMASUx3g%2Bx5Aw7v%2Bn0viWTBN6x0GWRCHv5jdJtaSPbHw3Ym4n2XJtv2UT8hHwxakiplrRaZNxy2DNB7s192ptG9DUKI4bmlVVodLJ%2F2GrdxrKQ8MncMI0qJPExNrRrfUIWc6t7uSvOrpBO4SDUvya%2FAw77T5l6403TXsUA3eBDQYy8%2FsYe66lGZ8hhHRb25c6efBREeth3Tgc2Z8LanyISfbkyTqeYznC0e2P7kZkXlEIBI%2BuzoKDvleIo3UrX%2BeOwRxw0PojS0FCWxRvmebw%2BiQWOqGw8x1Lb9tug%3D%3Db61311e1e7e83e618b7287ec23b49acf01b613d2',
      }
            self.params = {
      'uid': '79000822',
      'gm': 'local',
      'anyrewards': '',
      'anytarget': '',
      'task_id': '',
      'taskid': '',
      'taskkey': '',
      'taskvalue': '',
      'prisoncost': '',
      'studyatkvalue': '',
      'arrivalcount': '',
      'trade_num': '',
      'conquest_num': '',
      'conquest_tnum': '',
      'punishscore': '',
      'liveness': '',
      'achieveid': '',
      'stage': '',
      'achievevalue': '',
      'warhorserace_hscore': '',
      'warhorserace_score': '',
      'warhorserace_item': '',
      'warhorserace_attack': '',
      'warhorserace_rank': '',
      'acwarhorserace_attack_fuid': '',
      'acwarhorserace_score': '',
      'tctv': [
            '',
            '',
      ],
      'po': [
            '团长',
            '',
      ],
      'alliance_wealth': '',
      'alliance_exp': '',
      'alliance_lv': '',
      'boss_fuben[]': [
            '',
            '',
            '',
            '',
      ],
      'sboss_score': '',
      'boss_score': '',
      'search_num': '',
      'allServerRecharge_num': '',
      'modelname': '',
      'sql_name': '',
      'newyear-1': '',
      'prestige': '',
      'practice_exp': '',
      'monthcard': '',
      'yearcard': '',
      'vip_exp': '',
      'wifeskin_id': '',
      'servantskin_id': '',
      'activeinfo_id': '',
      'activeinfo_value': '',
      'crossdrawphone_buytime': '',
      'kinguid': '',
      'kingname': '',
      'king_st': '',
      'king_et': '',
      'train_lv': '',
      }
            

      # 生成 pid list (一般用于服务器生成的测试账号)
      def creat_pid_list(self, pid):
            result = []
            for i in range(100):
                  num = pid.split('test')[1]
                  num = int(num)
                  num += i
                  result.append('test' + str(num))
            return result


      # 获取pid对应服务器下的 uid(一般用于服务器生成的测试账号)
      def get_uid(self, pid_list, server):
            result = []
            for i in pid_list:
                  get_user_info = ClientMain.Client(i, server)
                  user_uid = get_user_info.GetAccessToken()[1]
                  result.append(user_uid)
            return result


      #  批量跳过用户新手引导
      def ContinueBeginnerTools(self, uid_list=[]):
            if not uid_list:
                  print('没有可执行的用户(uid不能为空)')
                  return None
            
            for each_uid in uid_list:
                  self.params['uid'] = each_uid
                  response = requests.get(
                  'http://192.168.8.83/gm/app/testtool/reset_userinfo/1/27',
                  params=self.params,
                  cookies=self.cooks,
                  headers=self.headers,
                  verify=False,
            )
                  result = response.text[1:42] + '}'
                  result = result.encode().decode('unicode_escape')
                  try:
                        result = json.loads(result)
                  except:
                        print(each_uid, '解码失败, 可能执行出错了, 跳过此用户')
                        continue
                  if result['ret'] == 0 and result['msg'] == '保存成功':
                        print(each_uid, '执行成功')
                        

      # 批量清空服务器所有活动
      def ClearAllServerActivity(self, uid=[]):
            if not uid:
                  print('没有可执行的用户(uid不能为空)')
                  return None
            for each_uid in uid:
                  self.params['uid'] = each_uid
                  respones = requests.get(
                        'http://192.168.8.83/gm/app/testtool/ajax_restsqltable/1',
                        headers=self.headers,
                        cookies=self.cooks,
                        params=self.params
                  )
                  result = respones.text[1:42] + '}'
                  result = json.loads(result)
                  if result['ret'] == 0 and result['msg'] == '保存成功':
                        print(each_uid, '执行成功')

      def increase_servant_level(self, uid):

            # 批量升级门客
            cookies = {
            'gdf_gm_session': 'aryD7HvOgapEg9Ms4KUd5jPopszk0YcBCysWsrVt9bJhuU8%2Fe9zGmqNXwOgJpdgdbp%2B1wvad5jByR5vz%2FbNLM2YetqidKsdc95JiewiAVPaRbMts4VCHfswz%2BnY3D%2F%2BYdgNNodCkyPBvoZ6jL3Jqk4ER28Tcd%2B%2BApI6OkUEhW1%2BmR9De9Y2O0%2FviavJJQ%2BxDii4Kgbx3EQGBi1i7lUxe1T13LUPSZS1gEtp%2Bv1eKXEvaFgTt9TYpeFNR0JzxvB1F%2BSnfNFoak5Bow3QEWVy0%2BZoW4ErfGb%2FsieicEOJqyCPskFcLPzQ%2FZKccgCIHLhUY57mtEzCyaS4vQCFMtHPhvAyjLLzBZAXcjNP%2BgaUFKnjsrpqIhvcvmPMDpp%2BlablVhivIScqnMBI3uzvSkARfQ%2FZ2uzXEX%2FXKthAADNI1Qjvrwxvf85z5MMxMm7S0kPQY3JuZwkJ4J3qFXacyrzoGggB6i8cdUcYrkAHGtbefuSEQs4abTRWzynvdaeGtJqUom2gTwGUZeqkZG%2FrwFT40rHSw86%2B8ByBBAQ1T2eX2BuQcszmioZQ4ECu8zyTsjrs8XH4pYscvIp6JRofhlDr5QQ%3D%3D2b8e83637df870e7971389aa4dd4263a6b1c12ea',
            }

            headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://192.168.8.83',
            'Referer': 'http://192.168.8.83/gm/app/role/show_servantinfo?uid=69000001&name=test81000002&zid=81&gm=local',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            # 'Cookie':                                                   'gdf_gm_session=aryD7HvOgapEg9Ms4KUd5jPopszk0YcBCysWsrVt9bJhuU8%2Fe9zGmqNXwOgJpdgdbp%2B1wvad5jByR5vz%2FbNLM2YetqidKsdc95JiewiAVPaRbMts4VCHfswz%2BnY3D%2F%2BYdgNNodCkyPBvoZ6jL3Jqk4ER28Tcd%2B%2BApI6OkUEhW1%2BmR9De9Y2O0%2FviavJJQ%2BxDii4Kgbx3EQGBi1i7lUxe1T13LUPSZS1gEtp%2Bv1eKXEvaFgTt9TYpeFNR0JzxvB1F%2BSnfNFoak5Bow3QEWVy0%2BZoW4ErfGb%2FsieicEOJqyCPskFcLPzQ%2FZKccgCIHLhUY57mtEzCyaS4vQCFMtHPhvAyjLLzBZAXcjNP%2BgaUFKnjsrpqIhvcvmPMDpp%2BlablVhivIScqnMBI3uzvSkARfQ%2FZ2uzXEX%2FXKthAADNI1Qjvrwxvf85z5MMxMm7S0kPQY3JuZwkJ4J3qFXacyrzoGggB6i8cdUcYrkAHGtbefuSEQs4abTRWzynvdaeGtJqUom2gTwGUZeqkZG%2FrwFT40rHSw86%2B8ByBBAQ1T2eX2BuQcszmioZQ4ECu8zyTsjrs8XH4pYscvIp6JRofhlDr5QQ%3D%3D2b8e83637df870e7971389aa4dd4263a6b1c12ea',
            }

            data = {
            'uid': '69000001',
            'servant_id': 'all',
            'gm': 'local',
            'action': 'update',
            'level': '101',
            'pill': '',
            'type': '1',
            'skillExp': '',
            'abilityExp': '',
            'trainExp': '',
            'abilityLv': '',
            'talentnum': '',
            }
            for each_uid in uid:
                  data['uid'] = each_uid
                  response = requests.post('http://192.168.8.83/gm/app/role/set_servant', cookies=cookies, headers=headers, data=data, verify=False)
                  result = response.text
                  if '0' in result:
                        print(each_uid, '执行成功')

      def query_pid(self, uid):
            # 查询uid对应的pid
            cookies = {
            'gdf_gm_session': 'zRPQ7Ogxju19P3tLleckrw3RPrTb0mQZ1O1QEc%2BZNhUSo0C9t5%2FrPJ1wclDn8ZlX%2BElED1y3kt2xh1nY14Yk404ksEoip8nb2Oj63lOm2of%2BA2HPSzW%2BcifgqNud46dUQ4lf2hGUEL7MgmSkTBMnn4qrEJu%2BZFMZNS3tNbb96WPQRZTGhcKFpHXOjNzxTNYKl52HPdoUoZRnfL84pUZzQCI2wiwyugpuvaMpcvOU4p8AbA3fSPY3VuFyUbiQlbG3ddW%2BE4n%2FL%2BlEpoxBHEzx52P5OkLKjaseKSMOew2bslsclBNdQAW9NurXeRQtrc14%2Bxv2jeCyyFc1B2Xgo%2BaDysEckkNYU9a1ofRCj%2BlsDvMexdmgxIMFY1jZoORUReRQR3ymicaixXb%2B2TmsUL6c85CsJrS1Jt0xB9qZBdSCwNkpfuC8l5IM4GDJuYNMQXzi2ipwXpGYQcQR0caqJkuDsVueH5LCvL%2Bxxkaj%2FOGp1ngTEiIlQa0oqFkD49%2FtR1CTeb%2BjmSHCWNqfMh7fAefMOTPSEoKgxrgowle9jRSoQq%2BXfs1t%2F19ya0kQ%2F3uQAJ6KTx%2BfZpbSWGnuMEcWvoeCVw%3D%3D285eaaa6c0aeec55e1e348c6468b2294c8552a40',
            }

            headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'http://192.168.8.83/gm/app/role/show_userinfo?gm=local',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
            # 'Cookie': 'gdf_gm_session=zRPQ7Ogxju19P3tLleckrw3RPrTb0mQZ1O1QEc%2BZNhUSo0C9t5%2FrPJ1wclDn8ZlX%2BElED1y3kt2xh1nY14Yk404ksEoip8nb2Oj63lOm2of%2BA2HPSzW%2BcifgqNud46dUQ4lf2hGUEL7MgmSkTBMnn4qrEJu%2BZFMZNS3tNbb96WPQRZTGhcKFpHXOjNzxTNYKl52HPdoUoZRnfL84pUZzQCI2wiwyugpuvaMpcvOU4p8AbA3fSPY3VuFyUbiQlbG3ddW%2BE4n%2FL%2BlEpoxBHEzx52P5OkLKjaseKSMOew2bslsclBNdQAW9NurXeRQtrc14%2Bxv2jeCyyFc1B2Xgo%2BaDysEckkNYU9a1ofRCj%2BlsDvMexdmgxIMFY1jZoORUReRQR3ymicaixXb%2B2TmsUL6c85CsJrS1Jt0xB9qZBdSCwNkpfuC8l5IM4GDJuYNMQXzi2ipwXpGYQcQR0caqJkuDsVueH5LCvL%2Bxxkaj%2FOGp1ngTEiIlQa0oqFkD49%2FtR1CTeb%2BjmSHCWNqfMh7fAefMOTPSEoKgxrgowle9jRSoQq%2BXfs1t%2F19ya0kQ%2F3uQAJ6KTx%2BfZpbSWGnuMEcWvoeCVw%3D%3D285eaaa6c0aeec55e1e348c6468b2294c8552a40',
            }

            params = {
            'uid': '61000010',
            'zid': '',
            'gm': 'local',
            }
            
            params['uid'] = uid
            response = requests.get(
            'http://192.168.8.83/gm/app/role/show_userinfo',
            params=params,
            cookies=cookies,
            headers=headers,
            verify=False,
            )



            soup = BeautifulSoup(response.text, 'lxml')

            # 定位 id 为 "pid" 的 input 标签
            pid_input = soup.find('input', {'id': 'pid'})
            if pid_input:
                  pid_value = pid_input.get('value')
                  #print(f"提取到的 PID: {pid_value}") 
            else:
                  print("未找到 pid 字段")
                  print(response.text)
            return pid_value
      

      def add_item(self, uid, item_id, item_num):

            if not isinstance(uid, list):
                  uid_list = []
                  uid_list.append(uid)
            else:
                  uid_list = []
                  uid_list.extend(uid)
            if not isinstance(item_id, list):
                  item_id_list = []
                  item_id_list.append(item_id)
            else:
                  item_id_list = []
                  item_id_list.extend(item_id)


            base_headers = {
                  "Accept": "*/*",
                  "Accept-Language": "zh-CN,zh;q=0.9",
                  "Connection": "keep-alive",
                  "Origin": "http://192.168.8.83",
                  "Referer": "http://192.168.8.83/gm/app/role/show_storage?uid=61000010&name=test61000010&zid=61&gm=local",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
                  "X-Requested-With": "XMLHttpRequest",}
            
            cookies = {
                  "gdf_gm_session": "XMxSY03vg%2Fdme9T8tS3MsorvfsFkfc%2F22IgEddcDmi5FFMaG4v7nKB0YrcE41muVGfSx6o8VeODp5ehB8t1YpcqArQWwN1LJ%2Ff9LouOv71RzozXKYV3eYFCrvzx7bPz8ta9u%2BsUzvrjAfJT0LKmGpJeRtnRJFXbXel1UcwBnRH8inJyyueSoeHU1g949toJ31vlMu7M1ZMMVgyTTjCVRz%2F9VxHzJOSiLf2pFA8ptVOUBe47JBf1E8k%2Bt%2FNvfLEoD6oDtckUEiWxnlRC5Wo9D78OHClUMPLWVIBhRRYirLrv9tGCJ4VhUddk7d5IUyPNzeIpAiBimPvPHbz5ru%2BI8G%2Bji9mUZlZE%2BxGGIqTCjsShl2HJbgGnbC06I%2BT4UkW9AlEJUCadfDS%2FiiNqzJWbZizaNt4X2aIsHgGQh6A26Tc%2FP2AFSF4F9SAjrTeE56O16zU1cs4ovh6QcDSXxF7M7vzXwCHaA3xcsF8vs6M0K%2BT24xvfc6MlusrLOO%2F%2Fwge972UYasEJfpWM9R2WBGjCLNMvkEgt7D9XiaD9%2F%2FjCdpB9%2FyJLbCHqijUT%2FRkKO82z4hUqSNtKnrSF6VQQblcaKoA%3D%3D3991eb1dbc5b6d4d9d7b010da104acd8ca6eb138"}

            for each_uid in uid_list:
                  for each_item in item_id_list:
                        payload = {
                        "uid": "86000001",
                        "gm": "local",
                        "itemNum": "拥有数量",
                        "num": "修改数量",
                        "typename": "1",
                        "num_1001": "1"}

                        payload["uid"] = str(each_uid)
                        del payload["num_1001"]
                        # 物品id
                        splice_id = "num_" + str(each_item)
                        payload[splice_id] = item_num
                        headers_json = base_headers.copy()
                        headers_json["Content-Type"] = "application/json; charset=UTF-8"
                        respone = requests.post('http://192.168.8.83/gm/app/role/update_storage/1', headers=headers_json, cookies=cookies, json=payload, verify=False, timeout=10)
                        #print(respone.text)
                        if '0' in respone.text:
                              print(each_uid, '执行成功')
                        del payload[splice_id]


      



if __name__ == '__main__':
      g = GmTools()

      # 生成test账号的pid
      pid_list = g.creat_pid_list('test1')

      # 获取test账号的uid
      uid_list = g.get_uid(pid_list, 78)

      # 批量跳过test 账号的新手引导
      #g.ContinueBeginnerTools(uid_list)

      # 批量清除服务器的所有活动, 一般在清理数据库后使用
      #g.ClearAllServerActivity([79000001, 80000001, 81000001])


      # 批量升级门客
      #g.increase_servant_level(uid_list)

      # 批量添加道具, 参数1: uid,  参数2: item id,  参数3: item 数量;   如果要给批量门客加批量道具, uid 和 item id 用列表形式传参
      g.add_item([81000011, 78000096, 61000018], [1001, 1002, 1003, 1004, 1005, 1006, 1007], 153)

      # 查询pid
      #g.query_pid(79000120)

