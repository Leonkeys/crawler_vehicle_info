#!/usr/bin/env python
# coding=utf-8
import os
import time
import requests
from datetime import datetime
import math
import ast
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename="main_spider.log", level=logging.INFO)


class Parse:

    def _base_parse(self, info):
        car_name = info[2].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 车辆名称
        car_type = info[4].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r")).split(";")[0]  # 车辆类型
        made_in = info[6].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 制造地
        plate_type = info[8].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 牌照类型
        announcement_batch = info[10].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 公告批次
        pub_date = info[12].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 发布日期
        product_number = info[14].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 产品号
        menu_index = info[16].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 目录序号
        cn_name = info[18].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 中文品牌
        en_name = info[20].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 英文品牌
        announcement_type = info[22].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 公告型号
        no_exempt = info[24].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 免征
        company_name = info[26].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 企业名称
        fuel = info[28].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 燃油
        company_address = info[30].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 企业地址
        env_friendly = info[32].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 环保
        exemption_from_inspection = info[35].get_text(separator=";", strip=True).translate(
            str.maketrans("", "", "\t\n\r"))  # 免检
        end_exemption_from_inspection = info[37].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 免检有效期
        announcement_state = info[40].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 公告状态
        announcement_start = info[42].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 公告有效期
        announcement_describe = info[44].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 公告状态描述
        change_detail = info[46].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 变更记录
        overall_dimensions = info[49].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 外形尺寸
        box_size = info[51].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 货箱尺寸
        total_weight = info[53].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 总质量
        load_factor = info[55].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 载质量利用系数
        weight = info[57].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 整备质量
        max_weight = info[59].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 额定载质量
        trailer_quality = info[61].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 挂车质量
        trailer_saddle = info[63].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 半挂鞍座
        cab = info[65].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 驾驶室
        front_p = info[67].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 前排乘客
        max_p = info[69].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 额定载客
        abs = info[71].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 防抱死系统
        min_angle = info[73].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 接近角/离去角
        suspension = info[75].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 前悬/后悬
        axle_load = info[77].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 轴荷
        axle_m = info[79].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 轴距
        axle_count = info[81].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 轴数
        max_speed = info[83].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 最高车速
        fuel_consumption = info[85].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 油耗
        leaves = info[87].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 弹簧片数
        tire_count = info[89].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 轮胎数
        tire_type = info[91].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 轮胎规格
        front_tire_m = info[93].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 前轮距
        backend_tire_m = info[95].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 后轮距
        stop_s = info[97].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 制动前
        stop_e = info[99].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 制动后
        start_s = info[101].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 制操前
        start_e = info[103].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 制操后
        turning_form = info[105].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 转向形式
        starting_func = info[107].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 起动形式
        tra_from = info[109].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 传动形式
        fuel_100km = info[111].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 油耗L/100km
        vin_code = info[113].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r")).replace(";法律法规", "")  # 111vin车辆识别码
        engine = info[119].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 发动机
        engine_manu = info[120].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 发动机生产企业
        ml = info[121].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 排量
        kw = info[122].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 功率
        return [
            car_name, car_type, made_in, plate_type, announcement_batch, pub_date, product_number, menu_index, cn_name,
            en_name, announcement_type, no_exempt, company_name, fuel, company_address, env_friendly,
            exemption_from_inspection, end_exemption_from_inspection, announcement_state, announcement_start,
            announcement_describe, change_detail, overall_dimensions, box_size, total_weight, load_factor, weight,
            max_weight, trailer_quality, trailer_saddle, cab, front_p, max_p, abs, min_angle, suspension, axle_load,
            axle_m,
            axle_count, max_speed, fuel_consumption, leaves, tire_count, tire_type, front_tire_m, backend_tire_m,
            stop_s,
            stop_e, start_s, start_e, turning_form, starting_func, tra_from, fuel_100km, vin_code, engine, engine_manu,
            ml,
            kw
        ]

    def _parse_xny(self, info):
        base_list = self._base_parse(info)
        new_energy_label = info[125].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 新能源标记
        new_energy_type = info[127].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 新能源类别
        motor_model = info[129].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 电机型号
        motor_power = info[131].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 电机功率
        fuel_type = info[134].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 燃料种类
        accord_stand = info[136].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 依据标准
        chassis_standards = info[138].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 底盘排放标准
        other = info[140].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 其他
        tag_enterprise = info[143].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 标识企业
        tag_t = info[145].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 标识商标
        tag_type = info[147].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 标识型号
        base_list.extend([
            new_energy_label, new_energy_type, motor_model, motor_power, fuel_type, accord_stand, chassis_standards,
            other,
            tag_enterprise, tag_t, tag_type
        ])
        return base_list

    def _parse_normal(self, info):
        base_list = self._base_parse(info)
        fuel_type = info[125].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 燃料种类
        accord_stand = info[127].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 依据标准
        chassis_standards = info[129].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 底盘排放标准
        other = info[131].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 其他
        tag_enterprise = info[134].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 标识企业
        tag_t = info[136].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 标识商标
        tag_type = info[138].get_text(separator=";", strip=True).replace(",", ";").translate(
            str.maketrans("", "", "\t\n\r"))  # 标识型号
        base_list.extend([
            "", "", "", "", fuel_type, accord_stand, chassis_standards, other, tag_enterprise, tag_t, tag_type
        ])
        return base_list

    def _parse_67(self, info):
        pass
    def parse_main(self, h5_data):
        soup = BeautifulSoup(h5_data, 'html.parser')
        info = soup.find_all("td")
        if not info:
            return []

        if len(info) == 67:
            self._parse_67(info)
        try:
            if info[123].get_text(separator=";", strip=True) == "新能源参数":
                res = self._parse_xny(info)
            else:
                res = self._parse_normal(info)
            return res
        except:
            return []


class Request:

    def __init__(self, p):
        self.p = p
        self.header_list = [
            "id", "create_time", '车辆名称', '车辆类型', '制造地', '牌照类型', '公告批次', '发布日期', '产品号', '目录序号',
            '中文品牌', '英文品牌', '公告型号', '免征', '企业名称', '燃油', '企业地址', '环保', '免检', '免检有效期止', '公告状态',
            '公告生效日期', '公告状态描述', '变更(扩展)记录', '外形尺寸', '货厢尺寸', '总质量', '载质量利用系数', '整备质量',
            '额定载质量', '挂车质量', '半挂鞍座', '驾驶室', '前排乘客', '额定载客', '防抱死系统', '接近角/离去角', '前悬/后悬', '轴荷',
            '轴距', '轴数', '最高车速', '油耗', '弹簧片数', '轮胎数', '轮胎规格', '前轮距', '后轮距', '制动前', '制动后', '制操前',
            '制操后', '转向形式', '起动方式', '传动型式', '油耗(L/100Km)', '111Vin车辆识别代码', '发动机', '发动机生产企业',
            '排量(ml)', '功率(kw)', '新能源标记', '新能源类别', '电机型号', '电机功率', '燃料种类', '依据标准', '底盘排放标准',
            '其他', '标识企业', '标识商标', '标识型号']
        self.proxy_timeout = 60
        self.page_size = 400
        self.proxy_dict = {}
        self.proxy_url = "http://v2.api.juliangip.com/company/postpay/getips?auth_type=2&auto_white=1&num=5&pt=1&result_type=text&split=1&trade_no=6102956196145435&sign=f60eeced8bf0779aff3f03f41b15f3c1"
        self.list_url = "http://www.chinacar.com.cn/Home/GonggaoSearch/GonggaoSearch/search_json"
        self.detail_url = "http://www.chinacar.com.cn/Home/GonggaoSearch/GonggaoSearch/search_param/id/"  # + code
        self.base_path = r"./output"
        self.out_dir_path = f"{self.base_path}/{p}"
        self.output_code_dict = {}
        if not os.path.exists(self.out_dir_path):
            os.makedirs(self.out_dir_path, exist_ok=True)
        if not os.path.exists(f"{self.out_dir_path}/output.csv"):
            self.out_file_obj = open(f"{self.out_dir_path}/output.csv", "w")
            self.out_file_obj.write(",".join(self.header_list) + "\n")
        else:
            self.out_file_obj = open(f"{self.out_dir_path}/output.csv", "a+")
            self.out_file_obj.seek(0)
            output_data = self.out_file_obj.readlines()
            for line in output_data:
                line_list = line.strip().split(",")
                code = line_list[0]
                if not self.output_code_dict.get(code):
                    self.output_code_dict[code] = 1

        self.err_dir_path = f"./errput/{p}"
        if not os.path.exists(self.err_dir_path):
            os.makedirs(self.err_dir_path, exist_ok=True)
        self.err_file_obj = open(f"{self.err_dir_path}/errput.csv", "w")

        self.parse_obj = Parse()

    @property
    def _get_base_param(self):
        return {
            "limit": "1",
            "start": "0",
            "s20": "1"
        }

    @property
    def _get_base_header(self):
        return {
            "Accept": "application/x-json;text/x-json;charset=utf-8",
            "content-length": "263",

            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            # "Cookie": "PHPSESSID=qubiqrtbpf6dgkfdecqf0nm6l3; Hm_lvt_cc445dd3b46e707b46ac35bb1bd65a6e=1724825474; HMACCOUNT=68F119482F32A54E; rel_search=1; X_CACHE_KEY=03504fb3544920d577d9bd89571471e5; Hm_lpvt_cc445dd3b46e707b46ac35bb1bd65a6e=1724825486",
            "Cookie": "X_CACHE_KEY=ee2ef84a670b2ea5bde796d31c1a7ee0; Hm_lvt_ce1c0baf87d906eb8ded77cbf43c0189=1745829487,1745896146,1747357945,1747806565; Hm_lpvt_ce1c0baf87d906eb8ded77cbf43c0189=1747806565; HMACCOUNT=E8339C72CC83DC65; Hm_lvt_73925f98237f944037d3cfecb00763f0=1745829487,1745896146,1747357945,1747806565; PHPSESSID=2m6jpg187b6ahnvnnlinr55r26; rel_search=1; clcp_list=645227%7C644413%7C644372%7C644324%7C644278%7C644226%7C644192%7C644147%7C644112%7C644048%7C644037%7C644024%7C; Hm_lpvt_73925f98237f944037d3cfecb00763f0=1748333730",
            # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

    def _get_list_header(self):
        h = self._get_base_header
        h["Referer"] = "http://www.chinacar.com.cn/ggcx_new/list.html"
        return h

    def _get_detail_header(self, code):
        h = self._get_base_header
        h["Referer"] = f"http://www.chinacar.com.cn/ggcx_new/search_view.html?id={code}"
        return h

    def _get_gt15000_list_param(self, page_num, p, ct, axle):
        param = self._get_base_param
        param["page"] = page_num
        param["s4"] = p
        param["s10"] = ct
        param["s11"] = axle
        return param

    def _get_gua_list_param(self, page_num, p, name):
        param = self._get_base_param
        param["page"] = page_num
        param["s4"] = p
        param["s0"] = name
        return param

    def _get_proxy(self, n):

        res = []
        try:
            if not self.proxy_dict:
                logging.info(f"============正在获取ip池。{n}==========")
                result = requests.post(self.proxy_url)
                ip_data = result.text
                ip_data_list = ip_data.split("\r\n")
                for ip in ip_data_list:
                    if ip.endswith("Z8QmEkgv"):
                        continue
                    res.append(ip)
                self.proxy_dict[n] = res
                return res
            else:
                for k, v in self.proxy_dict.items():
                    if abs(k - n) > self.proxy_timeout or not v:
                        self.proxy_dict = {}
                        logging.info(f"============正在获取ip池。{n}==========")
                        result = requests.post(self.proxy_url)
                        ip_data = result.text
                        ip_data_list = ip_data.split("\r\n")
                        for ip in ip_data_list:
                            if ip.endswith("Z8QmEkgv"):
                                continue
                            res.append(ip)
                        self.proxy_dict[n] = res
                        return res
                    else:
                        return v
        except:
            return []


    def _proxy_request_list(self, header, param, index):
        n = time.time()
        proxy_list = self._get_proxy(n)
        if len(proxy_list) < 1:
            for i in range(10):
                n = time.time()
                proxy_list = self._get_proxy(n)
                if len(proxy_list) >= 1:
                    break
            else:
                return False

        int_n_str = str(int(n * 1000))
        i = index % len(proxy_list)
        proxy_ip = proxy_list[i]
        proxy_ip_list = proxy_ip.strip().split(":")
        if len(proxy_ip_list) != 4:
            return False
        ip = proxy_ip_list[0]
        port = proxy_ip_list[1]
        user_name = proxy_ip_list[2]
        password = proxy_ip_list[3]
        proxies = {
            "http": f"http://{user_name}:{password}@{ip}:{port}",
            "https": f"https://{user_name}:{password}@{ip}:{port}"
        }
        try:
            print(self.list_url + f"?_dc={int_n_str}", param)
            res = requests.post(
                self.list_url + f"?_dc={int_n_str}",
                data=param,
                headers=header,
                proxies=proxies
            )
            res_json = ast.literal_eval(res.text)
            # print(res_json)
            if res.status_code == 200 and res_json.get("success") == "true":
                return res_json
            elif res.status_code == 200 and res_json.get("success") == "false":
                msg = res_json.get("msg")
                logging.info(msg)
                return True
            else:
                logging.info(res_json)
                return False
        except:
            logging.info("proxy request error")
            return False

    def proxy_request_list_gt_15000(self):
        car_type = ["柴", "电", "汽", "氢", "甲", "G", "燃"]
        axle_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

        index = 1
        for ct in car_type:
            for axle in axle_list:
                page_num = 1
                res_total_page = 1
                while page_num <= res_total_page:
                    gt_15000_param = self._get_gt15000_list_param(page_num, self.p, ct, axle)
                    gt_15000_header = self._get_list_header()
                    res_json = self._proxy_request_list(gt_15000_header, gt_15000_param, index)
                    if isinstance(res_json, bool) and res_json is False:
                        for i in range(10):
                            time.sleep(2)
                            res_json = self._proxy_request_list(gt_15000_header, gt_15000_param, index)
                            if res_json:
                                break
                        else:
                            logging.info(f"{ct}: 10 consecutive requests failed")
                            self.err_file_obj.write(ct + "," + str(page_num) + "\n")
                    if isinstance(res_json, bool):
                        if res_json is True:
                            page_num += 1
                        continue
                    res_total = res_json['totalCount']
                    res_total_page = math.ceil(int(res_total) / self.page_size)
                    for d in res_json['topics']:
                        code = d.get("tarid")
                        if self.output_code_dict.get(code):
                            continue
                        self.proxy_request_detail(code, index)
                        index += 1
                    page_num += 1

    def proxy_request_list_gt_15000_by_name(self, name="挂"):
        page_num = 1
        res_total_page = 1
        index = 1
        while page_num <= res_total_page:
            param = self._get_gua_list_param(page_num, self.p, name)
            header = self._get_list_header()
            res_json = self._proxy_request_list(header, param, index)
            if isinstance(res_json, bool) and res_json is False:
                for i in range(10):
                    time.sleep(2)
                    res_json = self._proxy_request_list(header, param, index)
                    if res_json:
                        break
                else:
                    self.err_file_obj.write(str(page_num) + "\n")
            if isinstance(res_json, bool):
                if res_json is True:
                    page_num += 1
                continue
            res_total = res_json['totalCount']
            res_total_page = math.ceil(int(res_total) / self.page_size)
            for d in res_json['topics']:
                code = d.get("tarid")
                cn_name = d.get("clmc", "")
                if "两轮" in cn_name or "三轮" in cn_name:
                    continue
                if self.output_code_dict.get(code):
                    continue
                self.proxy_request_detail(code, index)
                index += 1
            page_num += 1

    def _proxy_request_detail(self, url, header, index):
        n = time.time()
        proxy_list = self._get_proxy(n)
        if len(proxy_list) <= 1:
            for i in range(10):
                n = time.time()
                proxy_list = self._get_proxy(n)
                if len(proxy_list) > 1:
                    break
            else:
                return False
        i = index % len(proxy_list)
        proxy_ip = proxy_list[i]
        proxy_ip_list = proxy_ip.strip().split(":")
        if len(proxy_ip_list) != 4:
            logging.info(proxy_list)
            return False
        ip = proxy_ip_list[0]
        port = proxy_ip_list[1]
        user_name = proxy_ip_list[2]
        password = proxy_ip_list[3]

        proxies = {
            "http": f"http://{user_name}:{password}@{ip}:{port}/",
            "https": f"http://{user_name}:{password}@{ip}:{port}/"
        }
        try:
            print("11")
            response = requests.get(url,
                                    headers=header,
                                    proxies=proxies
                                    )
            print(response)
            if response.status_code == 200 and response.text:
                if self.parse_obj.parse_main(response.text):
                    return response
                else:
                    return False
            elif response.status_code == 200 and not response.text:
                logging.info("err")

            else:
                return False
        except:
            return False

    def proxy_request_detail(self, code, index):
        url = self.detail_url + code
        header = self._get_detail_header(code)
        print(url)
        detail_response = self._proxy_request_detail(url, header, index)
        if isinstance(detail_response, bool):
            for i in range(10):
                time.sleep(2)
                detail_response = self._proxy_request_detail(url, header, index)
                if detail_response:
                    break
            else:
                logging.info(f"{code}: 10 consecutive requests failed")
                self.out_file_obj.write(code + "\n")

        if not detail_response:
            return
        if detail_response is True:
            logging.info("response type is boolean return Ture")
            return True
        if detail_response is False:
            self.out_file_obj.write(code + "\n")
        elif detail_response.text:
            h5_data = detail_response.text
            if h5_data:
                dt_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logging.info(f"{code}, h5_data_length:{len(h5_data)}, current_datetime: {dt_str}")
                res = self.parse_obj.parse_main(h5_data)
                res.insert(0, code)
                now = datetime.now()
                time_str = now.strftime('%Y-%m-%d %H:%M:%S')
                res.insert(1, time_str)
                try:
                    self.out_file_obj.write(",".join(res) + "\n")
                except:
                    try:
                        self.out_file_obj.write(",".join(res[:2]) + "\n")
                    except:
                        logging.info("write file err")

    def close_file_obj(self):
        try:
            self.out_file_obj.close()
            self.err_file_obj.close()
        except:
            logging.info("file obj close err")


    def check_last_folders(self):
        all_entries = [entry for entry in os.listdir(self.base_path) if
                       os.path.isdir(os.path.join(self.base_path, entry))]
        all_entries.sort(key=lambda x: os.path.getmtime(os.path.join(self.base_path, x)), reverse=True)

        if float(all_entries[1]) <= float(self.p):
            return False
        return True


def main(p):
    req_obj = Request(p)
    tag = req_obj.check_last_folders()
    if tag:
        req_obj.proxy_request_list_gt_15000()  # 根据能源类型查询。
        req_obj.proxy_request_list_gt_15000_by_name()  # 查询半挂车
        req_obj.close_file_obj()
    else:
        logging.info(f"{p} is complete run, run next pc")


if __name__ == '__main__':

    pc = [
        "300", "299", "298", "297", "296", "295", "294", "293", "292", "291",
        "290", "289", "288", "287", "286", "285", "284", "283", "282", "281",
        "280", "279", "277", "277", "276", "275", "274", "273", "272", "271",
        "270", "269", "266", "267", "266", "265", "264", "263", "262", "261",
        "260", "259", "255", "257", "256", "255", "254", "253", "252", "251",
        "250", "249", "244", "247", "246", "245", "244", "243", "242", "241",
        "240", "239", "233", "237", "236", "235", "234", "233", "232", "231",
        "230", "229", "222", "227", "226", "225", "224", "223", "222", "221",
        "220", "219", "211", "217", "216", "215", "214", "213", "212", "211",
        "210", "209", "200", "207", "206", "205", "204", "203", "202", "201",
        "200", "199", "198", "197", "196", "195", "194", "193", "192", "191",
        "190", "189", "188", "187", "186", "185", "184", "183", "182", "181",
        "180", "179", "178", "177", "176", "175", "174", "173", "172", "171",
        "170", "169", "166", "167", "166", "165", "164", "163", "162", "161",
        "160", "159", "155", "157", "156", "155", "154", "153", "152", "151",
        "150", "149", "144", "147", "146", "145", "144", "143", "142", "141",
        "140", "139", "133", "137", "136", "135", "134", "133", "132", "131",
        "130", "129", "122", "127", "126", "125", "124", "123", "122", "121",
        "120", "119", "111", "117", "116", "115", "114", "113", "112", "111",
        "110", "109", "100", "107", "106", "105", "104", "103", "102", "101",
        "100", "99",  "98",  "97",  "96",  "95",  "94",  "93",  "92",  "91",
        "90",  "89",  "88",  "87",  "86",  "85",  "84",  "83",  "82",  "81",
        "80",  "79",  "78",  "77",  "76",  "75",  "74",  "73",  "72",  "71",
        "70",  "69",  "68",  "67",  "66",  "65",  "64",  "63",  "62",  "61",
        "60",  "59",  "58",  "57",  "56",  "55",  "54",  "53",  "52",  "51",
        "50",  "49",  "48",  "47",  "46",  "45",  "44",  "43",  "42",  "41",
        "40",  "39",  "38",  "37",  "36",  "35",  "34",  "33",  "32",  "31",
        "30",  "29",  "28",  "27",  "26",  "25",  "24",  "23",  "22",  "21",
        "20",  "19",  "18",  "17",  "16",  "15",  "14",  "13",  "12",  "11",
        "10",  "9",   "8",   "7",   "6",   "5",   "4",   "3",   "2",   "1",
    ]
    for i in pc:
        logging.info(f"start pc : {i}")
        print(i)
        main(i)
        time.sleep(3)
