#CHROME EC2
chrome_ec2 = {}
chrome_ec2['amiid'] = 'ami-id'
chrome_ec2['browserName'] = 'Chrome'
chrome_ec2['username'] = 'username'
chrome_ec2['ssh_key_path'] = '/path/to/.ssh/identity.pem'
chrome_ec2['hub_ip'] = 'localhost'
chrome_ec2['platform'] = 'LINUX'
chrome_ec2['launch'] = True
chrome_ec2['terminate'] = True
chrome_ec2['available_in_webserver'] = True
chrome_ec2['nb_instance'] = 3
chrome_ec2['nb_browser_by_instance'] = 1
chrome_ec2['max_number_of_instance'] = 20
chrome_ec2['ec2_region'] = 'us-east-1'
chrome_ec2['security_group_ids'] = ['security_group_id']
chrome_ec2['instance_type'] = 't2.micro'
chrome_ec2['selenium_command'] = "DISPLAY=:0 nohup java -jar selenium-server.jar -role node -hub http://{hub_ip}:4444/grid/register -browser browserName={browserName},maxInstances={nb_browser_by_instance},platform={platform} > node.log 2>&1 &"

#LOCALHOST FIREFOX
firefox_localhost = {}
firefox_localhost['browserName'] = 'Firefox'
firefox_localhost['highlight:use_highlight']= False
firefox_localhost['browser:window_width'] = 200
firefox_localhost['browser:window_height'] = 200

#LOCALHOST CHROME
chrome_localhost = {}
chrome_localhost['browserName'] = 'Chrome'

#LOCALHOST PHANTOMJS
phantomjs_localhost = {}
phantomjs_localhost['browserName'] = 'PhantomJS'
phantomjs_localhost['max_number_of_instance'] = 1

#MAIN CONFIG
browsers_config = {}
browsers_config['lfirefox'] = firefox_localhost
browsers_config['lf'] = firefox_localhost
browsers_config['lchrome'] = chrome_localhost
browsers_config['lphantomjs'] = phantomjs_localhost
browsers_config['chrome_ec2'] = chrome_ec2
