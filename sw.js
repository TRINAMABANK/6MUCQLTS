// Service worker stub to prevent 404 in dev environment
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', () => self.clients.claim());
