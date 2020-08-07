(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{61:function(e,t,r){"use strict";r.r(t),r.d(t,"frontMatter",(function(){return o})),r.d(t,"metadata",(function(){return s})),r.d(t,"rightToc",(function(){return c})),r.d(t,"default",(function(){return u}));var n=r(2),i=r(6),a=(r(0),r(73)),o={id:"authenticate",title:"Authentication / Authorization"},s={unversionedId:"authenticate",id:"authenticate",isDocsHomePage:!0,title:"Authentication / Authorization",description:"SPMT/AGORA",source:"@site/docs/authenticate.md",permalink:"/agora-sp/docs/",sidebar:"someSidebar",next:{title:"Profile Information",permalink:"/agora-sp/docs/profile"}},c=[{value:"SPMT/AGORA",id:"spmtagora",children:[]},{value:"Authentication",id:"authentication",children:[]},{value:"Authorization",id:"authorization",children:[{value:"User Roles",id:"user-roles",children:[]}]}],l={rightToc:c};function u(e){var t=e.components,r=Object(i.a)(e,["components"]);return Object(a.b)("wrapper",Object(n.a)({},l,r,{components:t,mdxType:"MDXLayout"}),Object(a.b)("h2",{id:"spmtagora"},"SPMT/AGORA"),Object(a.b)("p",null,"The Service Portfolio Management Tool (AGORA) is a tool aimed at facilitating service management in IT service provision, including federated scenarios.\nSPMT represents a complete list  of the services managed by a service provider; some of these services are visible to the customers, while others are internal.\nThe service management system has been designed to be compatible with the FitSM service portfolio management. ",Object(a.b)("a",Object(n.a)({parentName:"p"},{href:"https://fitsm.eu"}),"fitsm.eu")),Object(a.b)("h2",{id:"authentication"},"Authentication"),Object(a.b)("p",null,"Users can login with credentials provided by the administrator, or use the shibboleth login functionality to login with their academic account.\nAuthentication in SPMT supports federated AAI handled via SAML from the following providers:"),Object(a.b)("ul",null,Object(a.b)("li",{parentName:"ul"},"EGI AAI Check-in Service"),Object(a.b)("li",{parentName:"ul"},"EUDAT B2ACCESS"),Object(a.b)("li",{parentName:"ul"},"NI4OS Login service"),Object(a.b)("li",{parentName:"ul"},"VI-SEEM login")),Object(a.b)("h2",{id:"authorization"},"Authorization"),Object(a.b)("p",null,"The authorization in SPMT/AGORA follows the role-based access control. Role-based access control (RBAC) refers to the idea of assigning permissions to users based on their role within an organization. It provides fine-grained control and offers a simple, manageable approach to access management that is less prone to error than assigning permissions to users individually."),Object(a.b)("h3",{id:"user-roles"},"User Roles"),Object(a.b)("p",null,"It supports the following roles"),Object(a.b)("ul",null,Object(a.b)("li",{parentName:"ul"},Object(a.b)("strong",{parentName:"li"},"Super Admin"),": The one that administers the whole system"),Object(a.b)("li",{parentName:"ul"},Object(a.b)("strong",{parentName:"li"},"Admin"),": who can read/modify/delete everything"),Object(a.b)("li",{parentName:"ul"},Object(a.b)("strong",{parentName:"li"},"Resource admin"),": who can read everything; can modify/delete services that he is owner/manager of"),Object(a.b)("li",{parentName:"ul"},Object(a.b)("strong",{parentName:"li"},"Observer"),": who can read everything")),Object(a.b)("p",null,'A new user who has just registered in SPMT/AGORA, acquires only the right of access to the service as an observer. That is why it automatically enters the category of observer users. To grant more permissions, these it must be assigned by an "admin" or "superadmin" user. See below the categories of users that exist as well as their respective rights.'))}u.isMDXComponent=!0},73:function(e,t,r){"use strict";r.d(t,"a",(function(){return p})),r.d(t,"b",(function(){return d}));var n=r(0),i=r.n(n);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function s(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,i=function(e,t){if(null==e)return{};var r,n,i={},a=Object.keys(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(i[r]=e[r])}return i}var l=i.a.createContext({}),u=function(e){var t=i.a.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):s(s({},t),e)),r},p=function(e){var t=u(e.components);return i.a.createElement(l.Provider,{value:t},e.children)},b={inlineCode:"code",wrapper:function(e){var t=e.children;return i.a.createElement(i.a.Fragment,{},t)}},h=i.a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,a=e.originalType,o=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),p=u(r),h=n,d=p["".concat(o,".").concat(h)]||p[h]||b[h]||a;return r?i.a.createElement(d,s(s({ref:t},l),{},{components:r})):i.a.createElement(d,s({ref:t},l))}));function d(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var a=r.length,o=new Array(a);o[0]=h;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:n,o[1]=s;for(var l=2;l<a;l++)o[l]=r[l];return i.a.createElement.apply(null,o)}return i.a.createElement.apply(null,r)}h.displayName="MDXCreateElement"}}]);