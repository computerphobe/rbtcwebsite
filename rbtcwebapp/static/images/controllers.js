const about = (request, response, next) => {
    response.render('../views/pages/about',{
        title:'About Us',
        name:'About Us'
    })
}
const accounts = (request, response, next) => {
    response.render('../views/pages/accounts',{
        title:'Account',
        name:'Account'
    })
}
const applications = (request, response, next) => {
    response.render('../views/pages/applications',{
        title:'Application',
        name:'Application'
    })
}
const business = (request, response, next) => {
    response.render('../views/pages/business',{
        title:'Business',
        name:'Business'
    })
}
const contact = (request, response, next) => {
    response.render('../views/pages/contact',{
        title:'Contact',
        name:'Contact'
    })
}
const ecommerce = (request, response, next) => {
    response.render('../views/pages/ecommerce',{
        title:'Ecommerce',
        name:'Ecommerce'
    })
}
const employee = (request, response, next) => {
    response.render('../views/pages/employee',{
        title:'Employee',
        name:'Employee'
    })
}
const faq = (request, response, next) => {
    response.render('../views/pages/faq',{
        title:'Faq',
        name:'Faq'
    })
}
const index = (request, response, next) => {
    response.render('../views/pages/index',{
        title:'Index',
        name:'Index'
    })
}
const inventorie = (request, response, next) => {
    response.render('../views/pages/inventorie',{
        title:'Inventory',
        name:'Inventory'
    })
}
const landing = (request, response, next) => {
    response.render('../views/pages/landing',{
        title:'Landing',
        name:'Landing'
    })
}
const login = (request, response, next) => {
    response.render('../views/pages/login',{
        title:'Login',
        name:'Login'
    })
}
const ngo= (request, response, next) => {
    response.render('../views/pages/ngo',{
        title:'Ngo',
        name:'Ngo'
    })
}
const policy = (request, response, next) => {
    response.render('../views/pages/policy',{
        title:'Policy',
        name:'Policy'
    })
}
const portfolio = (request, response, next) => {
    response.render('../views/pages/portfolio',{
        title:'Portfolio',
        name:'Portfolio'
    })
}
const services = (request, response, next) => {
    response.render('../views/pages/services',{
        title:'Services',
        name:'Services'
    })
}
const shipping = (request, response, next) => {
    response.render('../views/pages/shipping',{
        title:'Shipping',
        name:'Shipping'
    })
}
const signup = (request, response, next) => {
    response.render('../views/pages/signup',{
        title:'Signup',
        name:'Signup'
    })
}
const terms = (request, response, next) => {
    response.render('../views/pages/terms',{
        title:'Terms',
        name:'Terms'
    })
}

module.exports = {   
    about,
    accounts,
    applications,
    business,
    contact,
    ecommerce,
    employee,
    faq,
    index,
    inventorie,
    landing,
    login,
    ngo,
    policy,
    portfolio,
    services,
    shipping,
    signup,
    terms
}