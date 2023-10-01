import requests
import time

# Hacker News APIのベースURLを定義
HN_API_BASE_URL = 'https://hacker-news.firebaseio.com/v0'


def get_top_stories(limit=30):
    # トップストーリーのIDを取得
    top_stories_ids = requests.get(f'{HN_API_BASE_URL}/topstories.json').json()
    # 結果を保存するための空のリストを初期化
    stories = []

    # トップストーリーのIDを順番に処理
    for story_id in top_stories_ids[:limit]:
        # APIに連続してアクセスしないように1秒待機
        time.sleep(1)
        # 各ストーリーの詳細データを取得
        story_data = requests.get(f'{HN_API_BASE_URL}/item/{story_id}.json').json()
        # タイトルとURLが存在する場合のみ、結果リストに追加
        if 'title' in story_data and 'url' in story_data:
            stories.append({'title': story_data['title'], 'link': story_data['url']})
            print(stories[-1])  # 最新のストーリーをターミナルに出力
    # 結果のリストを返す
    return stories


# スクリプトが直接実行された場合のみ以下を実行
if __name__ == '__main__':
    get_top_stories()
