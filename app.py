from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 景点数据示例
cities = {
    '哈尔滨': [
        {'name': '中央大街', 'lat': 45.7681, 'lon': 126.6208},
        {'name': '圣索菲亚大教堂', 'lat': 45.7733, 'lon': 126.6164},
        {'name': '太阳岛公园', 'lat': 45.8147, 'lon': 126.5350},
        {'name': '冰雪大世界', 'lat': 45.8006, 'lon': 126.5328},
        {'name': '哈尔滨极地馆', 'lat': 45.8141, 'lon': 126.5328},
        {'name': '龙塔', 'lat': 45.7411, 'lon': 126.6578},
        {'name': '东北虎林园', 'lat': 45.7860, 'lon': 126.6053},
        {'name': '伏尔加庄园', 'lat': 45.7084, 'lon': 126.8578},
        {'name': '兆麟公园', 'lat': 45.7698, 'lon': 126.6173},
        {'name': '松花江观光索道', 'lat': 45.7694, 'lon': 126.6265}
    ],
    #     "乌鲁木齐": [
    #     {"name": "天山天池", "lat": 43.9300, "lon": 88.1200},
    #     {"name": "红山公园", "lat": 43.8000, "lon": 87.6000},
    #     {"name": "大巴扎", "lat": 43.7700, "lon": 87.6200},
    #     {"name": "新疆博物馆", "lat": 43.8200, "lon": 87.5800},
    #     {"name": "南山风景区", "lat": 43.4500, "lon": 87.1800},
    #     {"name": "水磨沟公园", "lat": 43.8300, "lon": 87.6500},
    #     {"name": "达坂城古镇", "lat": 43.3800, "lon": 88.3000},
    #     {"name": "新疆国际大巴扎", "lat": 43.7700, "lon": 87.6200},
    #     {"name": "天山大峡谷", "lat": 43.4000, "lon": 87.1000},
    #     {"name": "新疆盐湖城景区", "lat": 43.5800, "lon": 87.7800}
    # ],
    #     "拉萨": [
    #     {"name": "布达拉宫", "lat": 29.6500, "lon": 91.1200},
    #     {"name": "大昭寺", "lat": 29.6600, "lon": 91.1400},
    #     {"name": "纳木错", "lat": 30.7600, "lon": 90.6000},
    #     {"name": "哲蚌寺", "lat": 29.6600, "lon": 91.1400},
    #     {"name": "罗布林卡", "lat": 29.6500, "lon": 91.1200},
    #     {"name": "小昭寺", "lat": 29.6600, "lon": 91.1400},
    #     {"name": "色拉寺", "lat": 29.6600, "lon": 91.1400},
    #     {"name": "甘丹寺", "lat": 29.6600, "lon": 91.1400},
    #     {"name": "羊卓雍错", "lat": 29.0000, "lon": 90.6000},
    #     {"name": "扎什伦布寺", "lat": 29.2300, "lon": 88.8800}
    # ]
    # 可以为其他城市添加类似的数据
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        days = int(request.form['days'])
        return redirect(url_for('itinerary', city=city, days=days))
    return render_template('index.html', cities=cities.keys())

@app.route('/itinerary/<city>/<int:days>')
def itinerary(city, days):
    attractions = cities.get(city, [])
    daily_plan = [attractions[i::days] for i in range(days)]
    daily_plan_with_day = list(enumerate(daily_plan, start=1))
    return render_template('itinerary.html', city=city, daily_plan=daily_plan_with_day)

if __name__ == '__main__':
    app.run(debug=True)
