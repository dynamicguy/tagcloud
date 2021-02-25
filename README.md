# jQuery tag cloud plugin
jQuery Tag Cloud looking like a 3d sphere. 3d animated tag cloud generated from an array. you can easily customize it by tweaking the params.

## Quick start
Here is an example for you. You can also view this demo [here](https://github.com/dynamicguy/tagcloud/).

```html
<!doctype html public "lice">
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!-- Consider adding a manifest.appcache: h5bp.com/d/Offline -->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
    <meta charset="utf-8">
    <title>jQuery tagcloud</title>
    <script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
    <script type="text/javascript" src="https://rawgithub.com/dynamicguy/tagcloud/master/src/tagcloud.jquery.js"></script>
    <style>
        /* Brute force CSS reset... */
        * {
            resize: none;
            border: none;
            outline: none;
            text-decoration: none;
            padding: 0px;
            margin: 0px;
            list-style-type: none;
        }
    </style>
  <script type="text/javascript">
      var settings = {
      //height of sphere container
      height: 400,
      //width of sphere container
      width: 400,
      //radius of sphere
      radius: 150,
      //rotation speed
      speed: 3,
      //sphere rotations slower
      slower: 0.9,
      //delay between update position
      timer: 5,
      //dependence of a font size on axis Z
      fontMultiplier: 15,
      //tag css stylies on mouse over
      hoverStyle: {
          border: 'none',
          color: '#0b2e6f'
      },
      //tag css stylies on mouse out
      mouseOutStyle: {
          border: '',
          color: ''
      }
      };

      $(document).ready(function(){
          $('#tagcloud').tagoSphere(settings);
      });
  </script>
</head>
<body>
<!-- Prompt IE 6 users to install Chrome Frame. Remove this if you support IE 6.
     chromium.org/developers/how-tos/chrome-frame-getting-started -->
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
    <div id="tagcloud">
        <ul>
            <li><a href="#">dazzlingly</a></li>
            <li><a href="#">natatory</a></li>
            <li><a href="#">automa</a></li>
            <li><a href="#">vinologist</a></li>
            <li><a href="#">castrate</a></li>
            <li><a href="#">airfoil</a></li>
            <li><a href="#">unpaintedly</a></li>
            <li><a href="#">caffetannic</a></li>
            <li><a href="#">fissirostrate</a></li>
            <li><a href="#">gingivectomy</a></li>
            <li><a href="#">pinprick</a></li>
            <li><a href="#">forecount</a></li>
            <li><a href="#">anorthophyre</a></li>
            <li><a href="#">tram</a></li>
            <li><a href="#">democratian</a></li>
            <li><a href="#">ungovernedness</a></li>
            <li><a href="#">anaesthesia</a></li>
            <li><a href="#">Eutychian</a></li>
            <li><a href="#">insalutary</a></li>
            <li><a href="#">amphilogism</a></li>
            <li><a href="#">reshunt</a></li>
            <li><a href="#">wende</a></li>
            <li><a href="#">ope</a></li>
            <li><a href="#">Bomarea</a></li>
        </ul>
    </div>
</body>
</html>
```

## demo

[![demo](https://github.com/dynamicguy/tagcloud/raw/master/test/screenshot.png)](https://github.com/dynamicguy/tagcloud/)

