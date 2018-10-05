webdav
=============

.. image:: https://travis-ci.org/kamikaze/webdav.svg?branch=master
    :target: https://travis-ci.org/kamikaze/webdav


Release Notes
=============

**Version 1.1.4 - 05.10.2018**
 * Handle HTTP 405 response code for MKCOL by https://github.com/kamikaze

**Version 1.1.2 - 07.06.2018**
 * Check for is_dir after confirmed that resource exists by https://github.com/kamikaze
 * Download remote file for open() only if it exists by https://github.com/kamikaze
 * Create directories recursively if file is being opened in write mode by https://github.com/kamikaze

**Version 1.1.1 - 07.06.2018**
 * Bug fixes by https://github.com/kamikaze

**Version 1.1.0 - 07.06.2018**
 * Added open() support for transparent file manipulations by https://github.com/kamikaze

**Version 1.0.0 - 06.06.2018**
 * Added support for custom authentication like NTLM by https://github.com/kamikaze
