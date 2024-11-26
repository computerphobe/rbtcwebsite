const express = require('express')
const router = express.Router()
const PageController = require('../controllers/admin')

router.get('/about', PageController.about);
router.get('/accounts', PageController.accounts);
router.get('/applications', PageController.applications);
router.get('/business', PageController.business);
router.get('/contact', PageController.contact);
router.get('/ecommerce', PageController.ecommerce);
router.get('/employee', PageController.employee);
router.get('/faq', PageController.faq);
router.get('/index', PageController.index);
router.get('/inventorie', PageController.inventorie);
router.get('/landing', PageController.landing);
router.get('/login', PageController.login);
router.get('/ngo', PageController.ngo);
router.get('/policy', PageController.policy);
router.get('/portfolio', PageController.portfolio);
router.get('/services', PageController.services);
router.get('/shipping', PageController.shipping);
router.get('/signup', PageController.signup);
router.get('/terms', PageController.terms);

module.exports = router