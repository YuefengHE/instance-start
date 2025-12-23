import os
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# 環境変数から設定を読み込む
api_key = os.environ.get('IBMCLOUD_API_KEY')
instance_id = os.environ.get('INSTANCE_ID')
action = os.environ.get('ACTION') # 'start' または 'stop'

def main():
    authenticator = IAMAuthenticator(api_key)
    service = VpcV1(authenticator=authenticator)
    
    if action == 'start':
        print(f"Starting instance: {instance_id}")
        service.create_instance_action(instance_id, 'start')
    elif action == 'stop':
        print(f"Stopping instance: {instance_id}")
        service.create_instance_action(instance_id, 'stop')

if __name__ == "__main__":
    main()