#!/usr/bin/python
# -*- coding: utf-8 -*-

import appindicator
import pynotify
import gtk
import gobject 
import socket
import time
import sys
import os


def checkStatus(item):
	global is_in_notify;
	is_in_notify=False;
	a.set_icon( os.path.abspath( "./1.png"));
	a.set_label("");
	pass

def quit(item):
	gtk.main_quit()



def update_clock():
	global a, sock,show_index,is_in_notify;
	#检查是否有信息到达
	data=""
	count=0;
	get_count=False;
	try:
		data,addr = sock.recvfrom(4096)	
		count=int(data);
		show_index=0;
		get_count=True;
		
	except:
		pass


	if ( get_count  ):
		if count == 0:
			is_in_notify=False;
			a.set_icon( os.path.abspath( "./1.png"));
			a.set_label("");
			
		else:
			is_in_notify=True;
			a.set_label(str(count));

	if ( is_in_notify ):
		show_index+=1;
		if (show_index%2==0):
			a.set_icon( os.path.abspath( "./1.png"));
			pass
		else:
			a.set_icon( os.path.abspath( "./2.png"));
			pass


	gobject.timeout_add(500,update_clock)
	pass

		

if __name__ == "__main__":
	
	a = appindicator.Indicator('wallch_indicator',  os.path.abspath( "./1.png"), appindicator.CATEGORY_APPLICATION_STATUS)
	a.set_status( appindicator.STATUS_ACTIVE )
	m = gtk.Menu()
	ci = gtk.MenuItem( '停止闪烁' )
	m.append(ci)
	
	a.set_menu(m)
	ci.show()
	
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.bind(('0.0.0.0',3008))
	sock.setblocking(0);
	
	
	show_index=0;
	is_in_notify=False;
	gobject.timeout_add(500, update_clock)
	ci.connect('activate',  checkStatus)
	os.chdir(os.path.dirname(sys.argv[0]))
	
	gtk.main()
