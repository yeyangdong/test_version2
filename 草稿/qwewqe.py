r_json={'status': 2000, 'message': 'need update',
         'result': {'app_name': '运维门户', 'binded': [], 'customer_status': True, 'last_ip': '10.65.66.102',
                    'app_id': 'tembin', 'create_time': '1601022572', 'partner': None, 'account_type': 'user',
                    'contact_name': 'tenant_2h', 'partner_id': None, 'account_name': 'tenant_2h',
                    'customer_name': '666_tx', 'original_ids': [], 'user_id': 'af8e4d59-64e0-3cde-973e-3277d2cdc955',
                    'parent_id': None, '_login_name': 'tenant_2h', 'op_user_id': '', 'last_login': 1606894195,
                    'formal': True, 'login_info_enable': 0, 'enable': True, 'first_time': 0,
                    'account_id': 'af8e4d59-64e0-3cde-973e-3277d2cdc955', 'account_source': 'pamc',
                    'account_role': 'customer_user', 'avatar_uploaded': False, 'login_source': 'web'}}

r_text={"status": 2000, "message": "need update", "result": {"app_name": "\u8fd0\u7ef4\u95e8\u6237", "binded": []}}


print(r_json['status'])
print(r_text['status'])
print(type(r_json))
print(type(r_text))

