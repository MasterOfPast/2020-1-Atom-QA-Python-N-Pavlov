class Urls:
	auth_url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
	localization_url = 'https://target.my.com/api/v2/localization_components.json?lang=en,ru'
	my_com = "https://target.my.com/auth/mycom?state=target_login%3D1#email"
	main_page = 'https://target.my.com/campaigns/list'
	good_url = 'http://mail.my.com/'
	bad_url = 'https://account.my.com/login/?error_code=1'
	csrf_url = 'https://target.my.com/csrf/'
	create_url = 'https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
	delete_url = 'https://target.my.com/api/v2/remarketing/segments/'