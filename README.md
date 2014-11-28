swift-middleware-sample
=======================

Sample code for an OpenStack Swift middleware, used during a talk at the OpenStack Atlanta summit:

https://www.youtube.com/watch?v=Y7YSuo1iwKU

https://www.openstack.org/assets/presentation-media/developing-your-own-swift-middleware.pdf

Please note, use only the following code in your Swift proxy server configuration for this middleware:

	[filter:middleware]
	use = egg:sample#middleware

You also need to install the middleware first:

	python setup.py install 
