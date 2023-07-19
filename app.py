from flask import abort, Flask, render_template

app = Flask(__name__, static_folder='static')

my_info = {
    "name": "岩本拓己",
    "affiliation": "大分工業高等専門学校 電気電子情報工学専攻",
    "email": "iwamototakumi000@gmail.com (個人) / aes2303@oita.kosen-ac.jp (学校)",
    "github": "iwamoto-takumi",
    "languages": {
        "Java": "14",
        "C / C++": "15",
        "HTML / CSS / JavaScript": "16",
        "Python": "17",
    },
    "clubs": ["ロボット研究部", "電子計算機部"],
    "github_url": "https://github.com/iwamoto-takumi",
}

projects = [
    {
        "id": 1,
        "title": "DensanTyping",
        "year": "本科1年",
        "tech": "Java + JavaFX",
        "abstract": "所属していた電子計算機部で、オープンキャンパスでの展示用に作成したタイピングゲーム。",
        "description": "私が本科の間に所属していた電子計算機部では、毎年オープンキャンパスでタイピング大会を開いてました。しかし、その時使われていたソフトはフリーソフトで、気になる問題点がありました。例えば、「しょ」を入力するには「syo」や「sho」、「silyo」などさまざまありますが、このうち1種類しか使えないという点です。この問題を解決し、実際に本科1年から3年の間までオープンキャンパスで使われ、多くの方に楽しんでもらえました。",
        "github": "https://github.com/iwamoto-takumi/DensanTyping"
    },
    {
        "id": 2,
        "title": "PacketAnalysis",
        "year": "本科4年",
        "tech": "Python + Scapy + PyQt5",
        "abstract": "授業で作成したネットワーク解析ソフト。",
        "description": "工学実験Ⅵの授業で、WireSharkより機能が少ないソフトウェアを作成しました。パケットキャプチャ、GUI、DBに分かれて作業を行い、最終的に成果物を完成することができました。",
        "github": "https://github.com/iwamoto-takumi/PacketAnalysis"
    },
    {
        "id": 3,
        "title": "Reminder Homework",
        "year": "専攻科1年",
        "tech": "Python + Pycord + MySQL",
        "abstract": "Discord上で動作する、課題の締切を通知してくれるBot。定期的な通知と、課題提出の1時間前の通知を行う。",
        "description": "本科から専攻科に進学後、課題が多くなりそれらの管理を行うために作成しました。クラスでDiscordのグループを作成しているため、そのグループ内でのみ運用しています。",
        "images": ["/static/images/reminder-bot.png"],
        "github": "https://github.com/iwamoto-takumi/ReminderHomework"
    },
    {
        "id": 4,
        "title": "ポートフォリオサイト",
        "year": "専攻科1年",
        "tech": "Python + Flask + Jinja2",
        "abstract": "ポートフォリオサイト。自分の作った成果物を紹介するためのサイト。",
        "description": "このポートフォリオサイトです。HTTPS通信を行うためにZeroSSLを使用しました。ホストは低価格なWebArenaを使用し、1つのインスタンスでポートフォリオ、SelfCount9、EnglishQuizの3つのサイトを公開するために、nginxのリバースプロキシの機能を利用しています。",
        "images": ["/static/images/portfolio.png"],
        "url": "https://portfolio.iwataku.site/",
        "github": "https://github.com/iwamoto-takumi/Portfolio"
    },
    {
        "id": 5,
        "title": "Task Tracker",
        "year": "専攻科1年",
        "tech": "C# + WPF + SQLite",
        "abstract": "簡易的なタスク管理ソフト。タスクの追加、完了、削除ができる。",
        "description": "単純なタスクの管理を行いたいのと、C#を使ってWindowsアプリを作成したいのとで、Windowsでのみ動作するタスク管理ソフトを作成しました。タスクの追加、完了、削除の最低限の機能を備えています。また、ClickOnceを使用して、簡易的なインストーラーを作成しました。",
        "images": ["/static/images/tasktracker-1.png", "/static/images/tasktracker-2.png"],
        "github": "https://github.com/iwamoto-takumi/TaskTracker"
    },
    {
        "id": 6,
        "title": "Self Count9",
        "year": "専攻科1年",
        "tech": "Python + Flask + Jinja2 + SQLite",
        "abstract": "ビリヤードのSelf Count9というルールのスコア管理サイト。",
        "description": "ビリヤードのスコア管理アプリはいくつかありますが、SelfCount9というルールのスコア管理アプリは見つからなかったため作成しました。開発期間は1週間程度で、初めてHTTPS通信を行うサイトを作成しました。HTTPS通信を行うために、ZeroSSLを用いてSSL証明書を取得しました。また、GoogleOAuthを利用してログイン機能を実装し、長期的なスコアの保存を可能にしました。",
        "images": ["/static/images/self-count9.png"],
        "url": "https://self-count9.iwataku.site/",
        "github": "https://github.com/iwamoto-takumi/SelfCount9"
    },
    {
        "id": 7,
        "title": "EnglishQuiz",
        "year": "専攻科1年",
        "tech": "Python + Flask + Jinja2",
        "abstract": "英単語のクイズを出題するサイト。",
        "description": "英語の授業で英単語テストがあったため、単語帳を持ち運ばなくてもスマホでどこでも学習ができるように作成しました。問題と答えが交互に出るモードと、4択問題が出るモードの2つを用意し、間違った問題のみやり直すことも可能です。",
        "images": ["/static/images/english-quiz.png"],
        "url": "http://english-quiz.iwataku.site/",
        "github": "https://github.com/iwamoto-takumi/EnglishQuiz"
    }
]


@app.route("/")
def index():
    return render_template("index.html", projects=projects, my_info=my_info)

@app.route("/project/<int:id>")
def project(id):
    project = next((project for project in projects if project["id"] == id), None)
    if project is None:
        abort(404)
    return render_template("project.html", project=project)

@app.route('/about_me')
def about_me():
    return render_template('about_me.html', my_info=my_info)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=10003)
