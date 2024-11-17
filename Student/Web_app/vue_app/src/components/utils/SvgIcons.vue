<template>
    <div class="svg_container" style="fill: black !important" v-html="currentSvg" />
</template>
<script>
export default {
    props: {
        icon: String,
        color: {
            default: '#000',
        }
    },
    computed: {
        currentSvg() {
            switch (this.icon) {
                case 'dot':
                    return this.svgDot();
                case 'add':
                    return this.svgAdd(this.color);
                case 'wallet':
                    return this.svgWallet(this.color);
                case 'subtract':
                    return this.svgSubtract(this.color);
                case 'dashboard':
                    return this.svgDashboard(this.color);
                case 'book':
                    return this.svgBook(this.color);
                case 'homework':
                    return this.svgHomeWork(this.color);
                case 'studentResults':
                    return this.svgStudentResults(this.color)
                case 'calender':
                    return this.svgCalender(this.color)
                case 'calenderEvent':
                    return this.svgCalenderEvent(this.color)
                case 'message':
                    return this.svgMessage(this.color)
                case 'settings':
                    return this.svgSettings(this.color)
                case 'expandRight':
                    return this.svgExpandRight(this.color)
                case 'expandLeft':
                    return this.svgExpandLeft(this.color)
                case 'person':
                    return this.svgPerson();
                case 'search':
                    return this.svgSearch()
                case 'people':
                    return this.svgPeople()
                case 'close':
                    return this.svgClose(this.color)
                case 'menu':
                    return this.svgMenu()
                case 'menu2':
                    return this.svgMenu2()
                case 'menu3':
                    return this.svgMenu3(this.color)
                case 'expand':
                    return this.svgExpand()
                case 'caretDown':
                    return this.svgCaretDown()
                case 'reset':
                    return this.svgReset()
                case 'checkBox':
                    return this.svgCheckBox()
                case 'checkMark':
                    return this.svgCheckMark(this.color)
                case 'pending':
                    return this.svgPending(this.color)
                case 'emptyBox':
                    return this.svgEmptyBox()
                case 'arrowUp':
                    return this.svgArrowUp()
                case 'arrowDown':
                    return this.svgArrowDown()
                case 'arrowLeft':
                    return this.svgArrowLeft()
                default:
                    return '';
            }
        }
    },
    methods: {
        svgDot() {
            return '<svg width="30px" height="30px" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path fill="#EE2924" d="M8 3a5 5 0 100 10A5 5 0 008 3z"></path></g></svg>'
        },
        svgWallet(color) {
            return `<svg viewBox="0 0 1024 1024" class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" fill="${color}"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M224 295.68c-42.24 0-64-21.76-64-64s21.76-64 64-64h665.6s25.6 0 25.6 25.6v102.4h-691.2z" fill="#C89005"></path><path d="M915.2 308.48h-691.2c-49.92 0-76.8-26.88-76.8-76.8s26.88-76.8 76.8-76.8h665.6c15.36 0 38.4 10.24 38.4 38.4v102.4c0 7.68-6.4 12.8-12.8 12.8z m-25.6-128h-665.6c-35.84 0-51.2 15.36-51.2 51.2s15.36 51.2 51.2 51.2h678.4v-89.6c0-10.24-7.68-12.8-12.8-12.8z" fill="#231C1C"></path><path d="M907.52 494.08c2.56 14.08-6.4 26.88-20.48 30.72l-601.6 122.88c-14.08 2.56-26.88-6.4-30.72-20.48l-74.24-363.52c-2.56-14.08 6.4-26.88 20.48-30.72l601.6-122.88c14.08-2.56 26.88 6.4 30.72 20.48l74.24 363.52z" fill="#C11F29"></path><path d="M280.32 660.48c-17.92 0-33.28-12.8-37.12-30.72l-74.24-363.52c-2.56-10.24 0-20.48 5.12-29.44 5.12-8.96 14.08-14.08 24.32-16.64l601.6-122.88c20.48-3.84 40.96 8.96 44.8 29.44l74.24 363.52c3.84 20.48-8.96 40.96-29.44 44.8l-601.6 122.88c-2.56 2.56-5.12 2.56-7.68 2.56z m527.36-537.6h-2.56l-601.6 122.88c-6.4 1.28-11.52 7.68-10.24 15.36l74.24 363.52c1.28 6.4 7.68 11.52 15.36 10.24l601.6-122.88c3.84-1.28 6.4-2.56 7.68-5.12 1.28-2.56 2.56-6.4 1.28-10.24L819.2 133.12c0-6.4-5.12-10.24-11.52-10.24z" fill="#231C1C"></path><path d="M860.16 263.68c1.28 8.96-7.68 19.2-21.76 21.76l-601.6 122.88c-14.08 2.56-26.88-2.56-28.16-11.52l-8.96-42.24c-1.28-8.96 7.68-19.2 21.76-21.76l601.6-122.88c14.08-2.56 26.88 2.56 28.16 11.52l8.96 42.24z" fill="#513328"></path><path d="M229.12 422.4c-16.64 0-30.72-8.96-33.28-23.04l-8.96-40.96c-3.84-16.64 10.24-33.28 32-37.12l601.6-122.88c20.48-3.84 39.68 5.12 43.52 21.76l8.96 42.24c3.84 16.64-10.24 33.28-32 37.12l-601.6 122.88h-10.24z m601.6-199.68h-5.12l-601.6 122.88c-7.68 1.28-11.52 5.12-11.52 7.68l8.96 40.96c1.28 1.28 6.4 2.56 12.8 1.28l601.6-122.88c7.68-1.28 11.52-5.12 11.52-6.4l-8.96-40.96c0-1.28-2.56-2.56-7.68-2.56zM513.1136 482.8928l112.8448-23.1808 5.1584 25.088-112.8576 23.168zM448.0768 548.2752l263.3216-54.08 5.1456 25.088-263.3216 54.08z" fill="#231C1C"></path><path d="M839.68 686.08c-3.84 14.08-17.92 21.76-32 16.64L183.04 512c-12.8-3.84-20.48-17.92-16.64-32l112.64-367.36c3.84-14.08 17.92-21.76 32-16.64l625.92 190.72c12.8 3.84 20.48 17.92 16.64 32l-113.92 367.36z" fill="#B8CA43"></path><path d="M815.36 718.08c-3.84 0-7.68 0-11.52-1.28L179.2 524.8c-10.24-2.56-17.92-10.24-23.04-19.2-5.12-8.96-5.12-19.2-2.56-29.44l112.64-367.36c6.4-20.48 26.88-32 47.36-25.6l625.92 190.72c20.48 6.4 30.72 28.16 25.6 47.36l-112.64 367.36c-2.56 10.24-8.96 17.92-17.92 23.04-6.4 3.84-12.8 6.4-19.2 6.4z m-512-610.56c-5.12 0-10.24 3.84-11.52 8.96L179.2 483.84c-1.28 3.84-1.28 6.4 1.28 10.24 1.28 2.56 3.84 5.12 7.68 6.4L812.8 691.2c2.56 1.28 6.4 0 8.96-1.28 2.56-1.28 5.12-3.84 6.4-7.68l112.64-367.36c2.56-6.4-1.28-14.08-7.68-15.36l-627.2-190.72c-1.28-1.28-1.28-1.28-2.56-1.28z" fill="#231C1C"></path><path d="M806.4 582.4l60.16-195.84c-26.88-7.68-40.96-37.12-33.28-64L375.04 183.04c-7.68 26.88-37.12 42.24-62.72 34.56l-60.16 195.84c26.88 7.68 40.96 37.12 33.28 64L742.4 616.96c8.96-26.88 37.12-42.24 64-34.56z" fill="#B8CA43"></path><path d="M751.36 632.32L270.08 485.12l3.84-12.8c2.56-10.24 2.56-20.48-2.56-29.44-5.12-8.96-12.8-15.36-21.76-17.92l-12.8-3.84 67.84-220.16 12.8 3.84c19.2 6.4 40.96-5.12 47.36-25.6l3.84-12.8 481.28 147.2-3.84 12.8c-2.56 10.24-2.56 20.48 2.56 29.44 5.12 8.96 12.8 15.36 21.76 17.92l12.8 3.84-67.84 220.16-12.8-3.84c-19.2-6.4-40.96 5.12-47.36 25.6l-3.84 12.8zM300.8 468.48l435.2 133.12c11.52-23.04 35.84-35.84 61.44-33.28l53.76-174.08c-10.24-6.4-19.2-15.36-25.6-25.6-6.4-11.52-7.68-23.04-6.4-35.84L384 199.68c-11.52 23.04-37.12 35.84-61.44 33.28L268.8 405.76c10.24 6.4 19.2 15.36 25.6 25.6 5.12 11.52 7.68 24.32 6.4 37.12z" fill="#231C1C"></path><path d="M506.440538 571.150982a163.84 179.2 17.002 1 0 104.797983-342.735967 163.84 179.2 17.002 1 0-104.797983 342.735967Z" fill="#E1E0A6"></path><path d="M550.4 590.08c-15.36 0-32-2.56-47.36-7.68-44.8-14.08-81.92-46.08-103.68-90.88-20.48-44.8-24.32-96-8.96-144.64 15.36-48.64 46.08-89.6 88.32-113.92 42.24-25.6 90.88-32 135.68-17.92 93.44 28.16 143.36 134.4 112.64 235.52-24.32 84.48-98.56 139.52-176.64 139.52z m16.64-355.84c-25.6 0-51.2 7.68-75.52 21.76-37.12 21.76-64 57.6-76.8 99.84s-10.24 87.04 7.68 125.44c17.92 38.4 48.64 65.28 87.04 76.8 79.36 24.32 166.4-26.88 193.28-115.2 26.88-88.32-16.64-179.2-96-203.52-11.52-2.56-25.6-5.12-39.68-5.12z" fill="#231C1C"></path><path d="M494.2464 567.4112l104.6528-342.784 24.4864 7.4752-104.6528 342.784z" fill="#231C1C"></path><path d="M540.16 537.6c-7.68 0-14.08-1.28-21.76-3.84-20.48-6.4-37.12-20.48-46.08-39.68-7.68-17.92-8.96-37.12-3.84-55.04l24.32 7.68c-3.84 12.8-2.56 25.6 2.56 37.12 6.4 12.8 16.64 23.04 30.72 26.88 26.88 7.68 55.04-7.68 62.72-34.56 7.68-26.88-6.4-55.04-33.28-64-39.68-12.8-62.72-55.04-49.92-96 6.4-19.2 19.2-35.84 37.12-44.8 17.92-10.24 38.4-11.52 57.6-6.4 19.2 6.4 35.84 19.2 44.8 37.12 8.96 17.92 11.52 38.4 5.12 58.88l-24.32-7.68c3.84-12.8 2.56-26.88-3.84-38.4-6.4-11.52-16.64-20.48-29.44-24.32-12.8-3.84-26.88-2.56-38.4 3.84-11.52 6.4-20.48 16.64-24.32 30.72-7.68 26.88 6.4 55.04 33.28 64 39.68 12.8 62.72 55.04 49.92 96-10.24 30.72-40.96 52.48-72.96 52.48z" fill="#231C1C"></path><path d="M953.6 782.08c0 14.08-11.52 25.6-25.6 25.6h-742.4c-14.08 0-25.6-11.52-25.6-25.6v-550.4c0 38.4 25.6 64 64 64h704c14.08 0 25.6 11.52 25.6 25.6v460.8z" fill="#00700d"></path><path d="M928 820.48h-742.4c-21.76 0-38.4-16.64-38.4-38.4v-550.4c0-7.68 5.12-12.8 12.8-12.8s12.8 5.12 12.8 12.8c0 30.72 20.48 51.2 51.2 51.2h704c21.76 0 38.4 16.64 38.4 38.4v460.8c0 21.76-17.92 38.4-38.4 38.4z m-755.2-529.92v491.52c0 7.68 5.12 12.8 12.8 12.8h742.4c7.68 0 12.8-5.12 12.8-12.8v-460.8c0-7.68-5.12-12.8-12.8-12.8h-704c-20.48 0-38.4-6.4-51.2-17.92z" fill="#231C1C"></path><path d="M953.6 615.68H803.84c-30.72 0-55.04-23.04-55.04-51.2v-25.6c0-28.16 24.32-51.2 55.04-51.2h151.04v128z" fill="#C89005"></path><path d="M953.6 628.48H803.84c-37.12 0-67.84-28.16-67.84-64v-25.6c0-35.84 30.72-64 67.84-64h151.04c7.68 0 12.8 5.12 12.8 12.8v128c-1.28 7.68-6.4 12.8-14.08 12.8z m-149.76-128c-23.04 0-42.24 16.64-42.24 38.4v25.6c0 21.76 19.2 38.4 42.24 38.4h138.24v-102.4H803.84z" fill="#231C1C"></path><path d="M226.56 346.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M328.96 346.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M431.36 346.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M533.76 346.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M636.16 346.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M738.56 346.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M840.96 346.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M226.56 730.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M328.96 730.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M431.36 730.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M533.76 730.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M636.16 730.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M738.56 730.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M840.96 730.88h61.44v25.6h-61.44z" fill="#231C1C"></path><path d="M812.8 551.68m-25.6 0a25.6 25.6 0 1 0 51.2 0 25.6 25.6 0 1 0-51.2 0Z" fill="#231C1C"></path></g></svg>`
        },
        svgAdd(color) {
            return `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <circle opacity="0.5" cx="12" cy="12" r="10" stroke="${color}" stroke-width="1.5"></circle> <path d="M15 12L12 12M12 12L9 12M12 12L12 9M12 12L12 15" stroke="${color}" stroke-width="1.5" stroke-linecap="round"></path> </g></svg>`
        },
        svgSubtract(color) {
            return `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <circle opacity="0.5" cx="12" cy="12" r="10" stroke="${color}" stroke-width="1.5"></circle> <path d="M15 12H9" stroke="${color}" stroke-width="1.5" stroke-linecap="round"></path> </g></svg>`
        },
        svgDashboard(color) {
            return `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M13 12C13 11.4477 13.4477 11 14 11H19C19.5523 11 20 11.4477 20 12V19C20 19.5523 19.5523 20 19 20H14C13.4477 20 13 19.5523 13 19V12Z" stroke="${color}" stroke-width="2" stroke-linecap="round"></path> <path d="M4 5C4 4.44772 4.44772 4 5 4H9C9.55228 4 10 4.44772 10 5V12C10 12.5523 9.55228 13 9 13H5C4.44772 13 4 12.5523 4 12V5Z" stroke="${color}" stroke-width="2" stroke-linecap="round"></path> <path d="M4 17C4 16.4477 4.44772 16 5 16H9C9.55228 16 10 16.4477 10 17V19C10 19.5523 9.55228 20 9 20H5C4.44772 20 4 19.5523 4 19V17Z" stroke="${color}" stroke-width="2" stroke-linecap="round"></path> <path d="M13 5C13 4.44772 13.4477 4 14 4H19C19.5523 4 20 4.44772 20 5V7C20 7.55228 19.5523 8 19 8H14C13.4477 8 13 7.55228 13 7V5Z" stroke="${color}" stroke-width="2" stroke-linecap="round"></path> </g></svg>`
        },
        svgBook(color){
            return `<svg fill="${color}" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M1750.21 0v1468.235h-225.882v338.824h169.412V1920H451.387c-82.447 0-161.506-36.141-214.701-99.388-43.934-51.953-67.652-116.33-67.652-182.965V282.353C169.034 126.494 295.528 0 451.387 0H1750.21Zm-338.823 1468.235H463.81c-89.223 0-166.136 59.86-179.576 140.047-1.242 9.036-2.259 18.07-2.259 27.106v2.26c0 40.658 13.553 77.928 40.659 109.552 32.753 38.4 79.059 59.859 128.753 59.859h960v-112.941H409.599v-112.942h1001.788v-112.94Zm225.882-1355.294H451.387c-92.725 0-169.412 75.67-169.412 169.412v1132.8c50.824-37.27 113.958-59.859 181.835-59.859h1173.46V112.941ZM1354.882 903.53v112.942H564.294V903.529h790.588Zm56.47-564.705v451.764H507.825V338.824h903.529Zm-112.94 112.94H620.765v225.883h677.647V451.765Z" fill-rule="evenodd"></path> </g></svg>`
        },
        svgHomeWork(color){
            return `<svg fill="${color}" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 496 496" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <g> <g> <path d="M0,0v432h64v32c0,17.648,14.352,32,32,32s32-14.352,32-32v-32h16v64h80v-40.208c6.704,5.08,14.96,8.208,24,8.208 c19.32,0,35.48-13.768,39.192-32H496V0H0z M112,464c0,8.824-7.176,16-16,16s-16-7.176-16-16v-16h32V464z M112,432H80v-16h32V432z M112,400H80V136h32V400z M81.328,120L96,95.544L110.672,120H81.328z M144,416h-16v-16h16V416z M208,96h-16v16h16v16h-32v16h32 v16h-16v16h16v16h-32v16h32v16h-16v16h16v16h-32v16h32v16h-16v16h16v16h-32v16h32v16h-16v16h16v16h-32v16h32v16h-16v16h16v16h-32 v16h32v16h-48V80h48V96z M144,64v320h-16V117.784L96,64.456l-32,53.328V384H48V48h192v336h-16V64H144z M480,416H272v8 c0,13.232-10.768,24-24,24s-24-10.768-24-24v-24h240V32H32v368h32v16H16V16h464V416z M256,384V48h192v336H256z"></path> <path d="M272,208h160V64H272V208z M288,80h128v112H288V80z"></path> <rect x="272" y="224" width="160" height="16"></rect> <rect x="272" y="256" width="160" height="16"></rect> <rect x="272" y="288" width="72" height="16"></rect> <rect x="360" y="288" width="72" height="16"></rect> <rect x="272" y="320" width="72" height="16"></rect> <rect x="360" y="320" width="72" height="16"></rect> <rect x="272" y="352" width="72" height="16"></rect> <rect x="416" y="352" width="16" height="16"></rect> <rect x="360" y="352" width="40" height="16"></rect> </g> </g> </g> </g></svg>`
        },
        svgStudentResults(color){
            return `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="${color}"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M16 10H8V9h8zm-4.87 11l1.064 1H3.5C2.122 22 1 20.43 1 18.5S2.122 15 3.5 15H5V5.75C5 3.682 6.122 2 7.5 2h13c1.378 0 2.45 1.57 2.45 3.5S21.878 9 20.5 9H19v7.138l-1 .979V5.75A5.994 5.994 0 0 1 18.64 3H7.5C6.792 3 6 4.176 6 5.75V15h10.57l-.71.826A4.141 4.141 0 0 0 15 18.5a5.186 5.186 0 0 0 .047.692l-1.032-.971A5.555 5.555 0 0 1 14.557 16H3.5C2.701 16 2 17.168 2 18.5S2.701 21 3.5 21zM19 8h1.5c.799 0 1.55-1.168 1.55-2.5S21.299 3 20.5 3h-.677A4.62 4.62 0 0 0 19 5.75zM8 13h8v-1H8zm8-7H8v1h8zm6.491 8.819l-6.998 6.851-2.832-2.663-.685.728 3.53 3.321 7.685-7.522z"></path><path fill="none" d="M0 0h24v24H0z"></path></g></svg>`
        },
        svgCalender(color){
            return `<svg fill="${color}" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M266.815 537.708c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.77 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.775 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.77 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zM266.815 679.347c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.77 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.775 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.77 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zM266.815 820.988c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.77 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.775 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zm182.77 0c0 22.62-18.34 40.96-40.96 40.96s-40.96-18.34-40.96-40.96 18.34-40.96 40.96-40.96 40.96 18.34 40.96 40.96zM228.18 81.918v153.6c0 11.311 9.169 20.48 20.48 20.48s20.48-9.169 20.48-20.48v-153.6c0-11.311-9.169-20.48-20.48-20.48s-20.48 9.169-20.48 20.48zm528.09 0v153.6c0 11.311 9.169 20.48 20.48 20.48s20.48-9.169 20.48-20.48v-153.6c0-11.311-9.169-20.48-20.48-20.48s-20.48 9.169-20.48 20.48z"></path><path d="M890.877 137.517c33.931 0 61.44 27.509 61.44 61.44v703.375c0 33.931-27.509 61.44-61.44 61.44h-757.76c-33.931 0-61.44-27.509-61.44-61.44V198.957c0-33.931 27.509-61.44 61.44-61.44h757.76zm-757.76 40.96c-11.309 0-20.48 9.171-20.48 20.48v703.375c0 11.309 9.171 20.48 20.48 20.48h757.76c11.309 0 20.48-9.171 20.48-20.48V198.957c0-11.309-9.171-20.48-20.48-20.48h-757.76z"></path><path d="M575.03 338.288c0-33.93-27.51-61.44-61.44-61.44s-61.44 27.51-61.44 61.44c0 33.93 27.51 61.44 61.44 61.44s61.44-27.51 61.44-61.44zm40.96 0c0 56.551-45.849 102.4-102.4 102.4s-102.4-45.849-102.4-102.4c0-56.551 45.849-102.4 102.4-102.4s102.4 45.849 102.4 102.4z"></path></g></svg>`
        },
        svgCalenderEvent(color){
            return `<svg fill="${color}" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <style type="text/css"> .st0{fill:none;} </style> <g> <path d="M20,7.4v10.5c0,1.7-1.3,3-3,3H5.9c0,1.1,0.9,2,2,2H18c2.2,0,4-1.8,4-4V9.4C22,8.3,21.1,7.4,20,7.4z"></path> <g> <path d="M5,1.1v2H4c-1.1,0-2,0.9-2,2v12c0,1.1,0.9,2,2,2h12.2c1.1,0,2-0.9,2-2v-12c0-1.1-0.9-2-2-2h-1v-2h-2v2H7v-2 C7,1.1,5,1.1,5,1.1z M4,8.1h12.2v9H4V8.1z"></path> <path d="M13.7,16.3l-2.4-1.4L9,16.3l0.6-2.7l-2.1-1.8l2.8-0.2L11.4,9l1.1,2.5l2.8,0.3l-2.1,1.8L13.7,16.3z"></path> </g> </g> <rect class="st0" width="24" height="24"></rect> </g></svg>`
        },
        svgMessage(color){
            return `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M7 9H17M7 13H17M21 20L17.6757 18.3378C17.4237 18.2118 17.2977 18.1488 17.1656 18.1044C17.0484 18.065 16.9277 18.0365 16.8052 18.0193C16.6672 18 16.5263 18 16.2446 18H6.2C5.07989 18 4.51984 18 4.09202 17.782C3.71569 17.5903 3.40973 17.2843 3.21799 16.908C3 16.4802 3 15.9201 3 14.8V7.2C3 6.07989 3 5.51984 3.21799 5.09202C3.40973 4.71569 3.71569 4.40973 4.09202 4.21799C4.51984 4 5.0799 4 6.2 4H17.8C18.9201 4 19.4802 4 19.908 4.21799C20.2843 4.40973 20.5903 4.71569 20.782 5.09202C21 5.51984 21 6.0799 21 7.2V20Z" stroke="${color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>`
        },
        svgSettings(color){
            return `<svg viewBox="0 0 30 30" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns" fill="${color}"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>settings</title> <desc>Created with Sketch Beta.</desc> <defs> </defs> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage"> <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-101.000000, -360.000000)" fill="${color}"> <path d="M128.52,381.134 L127.528,382.866 C127.254,383.345 126.648,383.508 126.173,383.232 L123.418,381.628 C122.02,383.219 120.129,384.359 117.983,384.799 L117.983,387 C117.983,387.553 117.54,388 116.992,388 L115.008,388 C114.46,388 114.017,387.553 114.017,387 L114.017,384.799 C111.871,384.359 109.98,383.219 108.582,381.628 L105.827,383.232 C105.352,383.508 104.746,383.345 104.472,382.866 L103.48,381.134 C103.206,380.656 103.369,380.044 103.843,379.769 L106.609,378.157 C106.28,377.163 106.083,376.106 106.083,375 C106.083,373.894 106.28,372.838 106.609,371.843 L103.843,370.232 C103.369,369.956 103.206,369.345 103.48,368.866 L104.472,367.134 C104.746,366.656 105.352,366.492 105.827,366.768 L108.582,368.372 C109.98,366.781 111.871,365.641 114.017,365.201 L114.017,363 C114.017,362.447 114.46,362 115.008,362 L116.992,362 C117.54,362 117.983,362.447 117.983,363 L117.983,365.201 C120.129,365.641 122.02,366.781 123.418,368.372 L126.173,366.768 C126.648,366.492 127.254,366.656 127.528,367.134 L128.52,368.866 C128.794,369.345 128.631,369.956 128.157,370.232 L125.391,371.843 C125.72,372.838 125.917,373.894 125.917,375 C125.917,376.106 125.72,377.163 125.391,378.157 L128.157,379.769 C128.631,380.044 128.794,380.656 128.52,381.134 L128.52,381.134 Z M130.008,378.536 L127.685,377.184 C127.815,376.474 127.901,375.749 127.901,375 C127.901,374.252 127.815,373.526 127.685,372.816 L130.008,371.464 C130.957,370.912 131.281,369.688 130.733,368.732 L128.75,365.268 C128.203,364.312 126.989,363.983 126.041,364.536 L123.694,365.901 C122.598,364.961 121.352,364.192 119.967,363.697 L119.967,362 C119.967,360.896 119.079,360 117.983,360 L114.017,360 C112.921,360 112.033,360.896 112.033,362 L112.033,363.697 C110.648,364.192 109.402,364.961 108.306,365.901 L105.959,364.536 C105.011,363.983 103.797,364.312 103.25,365.268 L101.267,368.732 C100.719,369.688 101.044,370.912 101.992,371.464 L104.315,372.816 C104.185,373.526 104.099,374.252 104.099,375 C104.099,375.749 104.185,376.474 104.315,377.184 L101.992,378.536 C101.044,379.088 100.719,380.312 101.267,381.268 L103.25,384.732 C103.797,385.688 105.011,386.017 105.959,385.464 L108.306,384.099 C109.402,385.039 110.648,385.809 112.033,386.303 L112.033,388 C112.033,389.104 112.921,390 114.017,390 L117.983,390 C119.079,390 119.967,389.104 119.967,388 L119.967,386.303 C121.352,385.809 122.598,385.039 123.694,384.099 L126.041,385.464 C126.989,386.017 128.203,385.688 128.75,384.732 L130.733,381.268 C131.281,380.312 130.957,379.088 130.008,378.536 L130.008,378.536 Z M116,378 C114.357,378 113.025,376.657 113.025,375 C113.025,373.344 114.357,372 116,372 C117.643,372 118.975,373.344 118.975,375 C118.975,376.657 117.643,378 116,378 L116,378 Z M116,370 C113.261,370 111.042,372.238 111.042,375 C111.042,377.762 113.261,380 116,380 C118.739,380 120.959,377.762 120.959,375 C120.959,372.238 118.739,370 116,370 L116,370 Z" id="settings" sketch:type="MSShapeGroup"> </path> </g> </g> </g></svg>`
        },
        svgExpandRight(color){
            return `<svg fill="${color}" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M1637.718 0c93.4 0 169.406 76.007 169.406 169.407v1581.13c0 93.512-76.007 169.407-169.406 169.407H451.87V0h1185.848zM1158.7 581l-79.861 79.861 242.422 242.423H667v112.94h654.262l-242.422 242.423 79.861 79.862 378.755-378.755L1158.7 581zM225.938 1920h112.938V.056H225.938z" fill-rule="evenodd"></path> </g></svg>`
        },
        svgExpandLeft(color){
            return `<svg fill="${color}" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M1807.124.056V1920h-112.938V.056h112.938ZM1468.254 0v1919.944H282.407c-93.4 0-169.407-75.895-169.407-169.407V169.407C113 76.007 189.007 0 282.407 0h1185.847ZM830.607 661.138 588.242 903.503h654.137v112.938H588.242l242.365 242.477-79.847 79.847-378.793-378.793 378.793-378.68 79.847 79.846Z" fill-rule="evenodd"></path> </g></svg>`
        },
        svgPerson() {
            return '<svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path fill-rule="evenodd" clip-rule="evenodd" d="M16.5 7.063C16.5 10.258 14.57 13 12 13c-2.572 0-4.5-2.742-4.5-5.938C7.5 3.868 9.16 2 12 2s4.5 1.867 4.5 5.063zM4.102 20.142C4.487 20.6 6.145 22 12 22c5.855 0 7.512-1.4 7.898-1.857a.416.416 0 0 0 .09-.317C19.9 18.944 19.106 15 12 15s-7.9 3.944-7.989 4.826a.416.416 0 0 0 .091.317z" fill="#ffffff"></path></g></svg>'
        },
        svgSearch() {
            return '<svg width="30px" height="30px" viewBox="0 -0.5 25 25" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M5.5 11.1455C5.49956 8.21437 7.56975 5.69108 10.4445 5.11883C13.3193 4.54659 16.198 6.08477 17.32 8.79267C18.4421 11.5006 17.495 14.624 15.058 16.2528C12.621 17.8815 9.37287 17.562 7.3 15.4895C6.14763 14.3376 5.50014 12.775 5.5 11.1455Z" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M15.989 15.4905L19.5 19.0015" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>'
        },
        svgPeople() {
            return '<svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M17.5291 7.77C17.4591 7.76 17.3891 7.76 17.3191 7.77C15.7691 7.72 14.5391 6.45 14.5391 4.89C14.5391 3.3 15.8291 2 17.4291 2C19.0191 2 20.3191 3.29 20.3191 4.89C20.3091 6.45 19.0791 7.72 17.5291 7.77Z" fill="#ffffff"></path> <path d="M20.7916 14.7004C19.6716 15.4504 18.1016 15.7304 16.6516 15.5404C17.0316 14.7204 17.2316 13.8104 17.2416 12.8504C17.2416 11.8504 17.0216 10.9004 16.6016 10.0704C18.0816 9.8704 19.6516 10.1504 20.7816 10.9004C22.3616 11.9404 22.3616 13.6504 20.7916 14.7004Z" fill="#ffffff"></path> <path d="M6.44016 7.77C6.51016 7.76 6.58016 7.76 6.65016 7.77C8.20016 7.72 9.43016 6.45 9.43016 4.89C9.43016 3.29 8.14016 2 6.54016 2C4.95016 2 3.66016 3.29 3.66016 4.89C3.66016 6.45 4.89016 7.72 6.44016 7.77Z" fill="#ffffff"></path> <path d="M6.55109 12.8506C6.55109 13.8206 6.76109 14.7406 7.14109 15.5706C5.73109 15.7206 4.26109 15.4206 3.18109 14.7106C1.60109 13.6606 1.60109 11.9506 3.18109 10.9006C4.25109 10.1806 5.76109 9.89059 7.18109 10.0506C6.77109 10.8906 6.55109 11.8406 6.55109 12.8506Z" fill="#ffffff"></path> <path d="M12.1208 15.87C12.0408 15.86 11.9508 15.86 11.8608 15.87C10.0208 15.81 8.55078 14.3 8.55078 12.44C8.56078 10.54 10.0908 9 12.0008 9C13.9008 9 15.4408 10.54 15.4408 12.44C15.4308 14.3 13.9708 15.81 12.1208 15.87Z" fill="#ffffff"></path> <path d="M8.87078 17.9406C7.36078 18.9506 7.36078 20.6106 8.87078 21.6106C10.5908 22.7606 13.4108 22.7606 15.1308 21.6106C16.6408 20.6006 16.6408 18.9406 15.1308 17.9406C13.4208 16.7906 10.6008 16.7906 8.87078 17.9406Z" fill="#ffffff"></path> </g></svg>'
        },
        svgClose(color) {
            return `<svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path fill-rule="evenodd" clip-rule="evenodd" d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12ZM8.96963 8.96965C9.26252 8.67676 9.73739 8.67676 10.0303 8.96965L12 10.9393L13.9696 8.96967C14.2625 8.67678 14.7374 8.67678 15.0303 8.96967C15.3232 9.26256 15.3232 9.73744 15.0303 10.0303L13.0606 12L15.0303 13.9696C15.3232 14.2625 15.3232 14.7374 15.0303 15.0303C14.7374 15.3232 14.2625 15.3232 13.9696 15.0303L12 13.0607L10.0303 15.0303C9.73742 15.3232 9.26254 15.3232 8.96965 15.0303C8.67676 14.7374 8.67676 14.2625 8.96965 13.9697L10.9393 12L8.96963 10.0303C8.67673 9.73742 8.67673 9.26254 8.96963 8.96965Z" fill="${color}"></path></g></svg>`;
        },
        svgMenu() {
            return '<svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 6H20M7 12H17M9 18H15" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>'
        },
        svgMenu2() {
            return '<svg viewBox="64 64 896 896" focusable="false" data-icon="ellipsis" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M176 511a56 56 0 10112 0 56 56 0 10-112 0zm280 0a56 56 0 10112 0 56 56 0 10-112 0zm280 0a56 56 0 10112 0 56 56 0 10-112 0z"></path></svg>'
        },
        svgMenu3(color) {
            return `<svg width="64px" height="64px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="${color}"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g id="icomoon-ignore"> </g> <path d="M3.205 6.937v4.265h25.59v-4.265h-25.59zM27.729 10.136h-23.457v-2.133h23.457v2.133z" fill="${color}"> </path> <path d="M3.205 18.133h25.59v-4.265h-25.59v4.265zM4.271 14.934h23.457v2.133h-23.457v-2.133z" fill="${color}"> </path> <path d="M3.205 25.063h25.59v-4.265h-25.59v4.265zM4.271 21.864h23.457v2.133h-23.457v-2.133z" fill="${color}"> </path> </g></svg>`
        },
        svgExpand() {
            return '<svg fill="#ffffff" width="30px" height="30px" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M3,4V20a1,1,0,0,0,1,1H20a1,1,0,0,0,1-1V4a1,1,0,0,0-1-1H4A1,1,0,0,0,3,4ZM5,5H19V19H10V15a1,1,0,0,0-1-1H5Zm6.293,7.707a1,1,0,0,1,0-1.414L14.086,8.5H13a1,1,0,0,1,0-2h3.5a1.01,1.01,0,0,1,.382.077A1,1,0,0,1,17.5,7.5V11a1,1,0,0,1-2,0V9.914l-2.793,2.793A1,1,0,0,1,11.293,12.707Z"></path></g></svg>'
        },
        svgCaretDown() {
            return '<svg fill="#ffffff" viewBox="0 0 256 256" id="Flat" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M128,180a3.98881,3.98881,0,0,1-2.82861-1.17139l-80-80.00024a4.00009,4.00009,0,0,1,5.65722-5.65674L128,170.34326l77.17139-77.17163a4.00009,4.00009,0,0,1,5.65722,5.65674l-80,80.00024A3.98881,3.98881,0,0,1,128,180Z"></path> </g></svg>'
        },
        svgReset() {
            return '<svg fill="#ffffff" width="64px" height="64px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M960 0v213.333c411.627 0 746.667 334.934 746.667 746.667S1371.627 1706.667 960 1706.667 213.333 1371.733 213.333 960c0-197.013 78.4-382.507 213.334-520.747v254.08H640V106.667H53.333V320h191.04C88.64 494.08 0 720.96 0 960c0 529.28 430.613 960 960 960s960-430.72 960-960S1489.387 0 960 0" fill-rule="evenodd"></path> </g></svg>'
        },
        svgCheckBox() {
            return '<svg fill="#ffffff" width="64px" height="64px" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title>ionicons-v5-l</title><path d="M400,48H112a64.07,64.07,0,0,0-64,64V400a64.07,64.07,0,0,0,64,64H400a64.07,64.07,0,0,0,64-64V112A64.07,64.07,0,0,0,400,48ZM364.25,186.29l-134.4,160a16,16,0,0,1-12,5.71h-.27a16,16,0,0,1-11.89-5.3l-57.6-64a16,16,0,1,1,23.78-21.4l45.29,50.32L339.75,165.71a16,16,0,0,1,24.5,20.58Z"></path></g></svg>'
        },
        svgCheckMark(color) {
            return `<svg viewBox="0 0 24.00 24.00" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="${color}" stroke-width="0.00024000000000000003"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M17.8086 9.70558C18.1983 9.31421 18.1969 8.68105 17.8056 8.29137C17.4142 7.90169 16.781 7.90305 16.3913 8.29442L10.6215 14.0892L7.30211 10.816C6.90886 10.4283 6.27571 10.4327 5.88793 10.8259C5.50015 11.2192 5.50459 11.8524 5.89784 12.2401L9.92581 16.212C10.3177 16.5985 10.9482 16.5956 11.3366 16.2056L17.8086 9.70558Z" fill="${color}"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M12 1C5.92487 1 1 5.92487 1 12C1 18.0751 5.92487 23 12 23C18.0751 23 23 18.0751 23 12C23 5.92487 18.0751 1 12 1ZM3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12Z" fill="${color}"></path> </g></svg>`
        },
        svgPending(color) {
            return `<svg viewBox="0 0 1024 1024" class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" fill="#000000" stroke="#000000" stroke-width="0.01024"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M511.9 183c-181.8 0-329.1 147.4-329.1 329.1s147.4 329.1 329.1 329.1c181.8 0 329.1-147.4 329.1-329.1S693.6 183 511.9 183z m0 585.2c-141.2 0-256-114.8-256-256s114.8-256 256-256 256 114.8 256 256-114.9 256-256 256z" fill="${color}"></path><path d="M548.6 365.7h-73.2v161.4l120.5 120.5 51.7-51.7-99-99z" fill="${color}"></path></g></svg>`
        },
        svgEmptyBox() {
            return '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M6 5C5.44772 5 5 5.44772 5 6V13V18C5 18.5523 5.44772 19 6 19H18C18.5523 19 19 18.5523 19 18V13V6C19 5.44772 18.5523 5 18 5H6ZM3 6C3 4.34315 4.34315 3 6 3H18C19.6569 3 21 4.34315 21 6V13V18C21 19.6569 19.6569 21 18 21H6C4.34315 21 3 19.6569 3 18V13V6Z" fill="#ffffff"></path> </g></svg>'
        },
        svgArrowUp() {
            return '<svg width="64px" height="64px" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M6 8L2 8L2 6L8 5.24536e-07L14 6L14 8L10 8L10 16L6 16L6 8Z" fill="#ffffff"></path> </g></svg>'
        },
        svgArrowDown() {
            return '<svg width="64px" height="64px" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M10 8L14 8V10L8 16L2 10V8H6V0L10 4.76995e-08V8Z" fill="#ffffff"></path> </g></svg>'
        },
        svgArrowLeft() {
            return '<svg fill="#737373" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" stroke="#737373"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M222.927 580.115l301.354 328.512c24.354 28.708 20.825 71.724-7.883 96.078s-71.724 20.825-96.078-7.883L19.576 559.963a67.846 67.846 0 01-13.784-20.022 68.03 68.03 0 01-5.977-29.488l.001-.063a68.343 68.343 0 017.265-29.134 68.28 68.28 0 011.384-2.6 67.59 67.59 0 0110.102-13.687L429.966 21.113c25.592-27.611 68.721-29.247 96.331-3.656s29.247 68.721 3.656 96.331L224.088 443.784h730.46c37.647 0 68.166 30.519 68.166 68.166s-30.519 68.166-68.166 68.166H222.927z"></path></g></svg>'
        },

    },
}
</script>

<style>
.svg_container {
    width: fit-content;
    height: fit-content;
}

svg {
    width: var(--svg-width) !important;
    height: var(--svg-height) !important;
    margin: var(--svg-margin) !important;
    padding: var(--svg-padding) !important;
    cursor: var(--svg-cursor) !important;
    transform: var(--svg-transform) !important;
}
</style>