import os
import sys
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

# 1. 環境変数から設定を読み込む（コードに直接書かない！）
API_KEY = os.getenv('IBM_CLOUD_API_KEY')
INSTANCE_ID = os.getenv('INSTANCE_ID')
REGION = os.getenv('REGION', 'us-dal')

if not API_KEY or not INSTANCE_ID:
    print("Error: 環境変数 IBM_CLOUD_API_KEY と INSTANCE_ID が必要です。")
    sys.exit(1)

try:
    # 2. 認証とクライアントの初期化
    authenticator = IAMAuthenticator(API_KEY)
    service = VpcV1(authenticator=authenticator)
    service.set_service_url(f'https://{REGION}.iaas.cloud.ibm.com/v1')

    # 3. インスタンスの状態を確認（オプション）
    instance = service.get_instance(id=INSTANCE_ID).get_result()
    print(f"現在のステータス: {instance['status']}")

    if instance['status'] == 'running':
        print("インスタンスは既に起動しています。")
    else:
        # 4. 起動リクエスト (start)
        print(f"インスタンス {INSTANCE_ID} を起動します...")
        response = service.create_instance_action(
            instance_id=INSTANCE_ID,
            type='start'
        ).get_result()
        print("起動リクエストを送信しました。")

except ApiException as e:
    print(f"APIエラーが発生しました: {e.code} - {e.message}")
    sys.exit(1)
except Exception as e:
    print(f"予期せぬエラー: {e}")
    sys.exit(1)
