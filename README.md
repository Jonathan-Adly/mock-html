# mock-html
mock-html is a web server powered by Django and htmx that provides mock HTML responses for experimenting with htmx or other hypermedia libraries. It allows you to simulate server responses and test client-side rendering without the need for a real backend. 

# why?

If you are hacking a prototype or following a tutorial with a hypermedia library (htmx and similar), you have to spin up a web server just to see something.

I didn't like the friction and the time it needed just to explain how it works to a new developer who is used to working with JSON. I spent more time getting a web server up than actually explaining things (htmx is dead-simple!).

This mock-html server simply returns html fragments as you request them. Hit the server with /tag/{html tag name} - and you get mock html fragments back. You can add custom classes as well. It will also mock POST/PUT/DELETE for you. 

Also - this works well if you want to use your own custom html fragment. Just make a public <a href="https://gist.github.com/"> github gist </a> and hit the server with the gist id. You can totally use this in all kinds of crazy ways.

You can find it running here and are free to use it in your developments: https://html-mock.fly.dev/.

I hope you will find it useful.

## Table of Contents
- [Getting Started](#getting-started)
  - [Getting a Resource](#getting-a-resource)
  - [Posting a Resource](#posting-a-resource)
  - [PUT Request](#put-request)
  - [Delete Request](#delete-request)
  - [Adding Classes](#adding-classes)
  - [Your Own Data](#your-own-data)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

If you want to spin up your own server, clone the repo and `python manage.py runserver`. As always, don't forget to manage your python environments. Also, you will need a db.sqlite3 as tags are stored there for ease of development.

Otherwise, simply make requests to the server at `https://html-mock.fly.dev/` and you will get html back.

<h2> Documentation </h2>
<h4 id="get"> Getting a resource </h4>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;!-- adjust htmx attributes for your own needs --&gt;
            &lt;button
            hx-get=&quot;https://html-mock.fly.dev/tag/table&quot;
            hx-target=&quot;#results&quot;
            hx-swap=&quot;innerHTML&quot;
            hx-trigger=&quot;click&quot;
            &gt; Get Table &lt;/button&gt;
        </code>
      </pre>
    <p> 👇 Output </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;table&gt;
            &lt;tr&gt;
              &lt;th&gt;Header 1&lt;/th&gt;
              &lt;th&gt;Header 2&lt;/th&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
              &lt;td&gt;Data 1&lt;/td&gt;
              &lt;td&gt;Data 2&lt;/td&gt;
            &lt;/tr&gt;
          &lt;/table&gt;
        </code>
      </pre>
    <br>
<h4 id="post"> Posting a resource </h4>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;!-- make sure you fill out other htmx attributes as needed --&gt;
            &lt;form hx-post=&quot;https://html-mock.fly.dev/tag/paragraph&quot;&gt;
            &lt;label for=&quot;name&quot;&gt;Name:&lt;/label&gt;
            &lt;input type=&quot;text&quot; id=&quot;name&quot; name=&quot;name&quot; value=&quot;foo&quot;&gt;
            &lt;input type=&quot;submit&quot; value=&quot;Submit&quot;&gt;
            &lt;/form&gt;
        </code>
      </pre>
    <p> 👇 Output </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
           &lt;p&gt; &lt;span&gt; You Posted the following values: foo &lt;/span&gt; Lorem Ipsum &lt;/p&gt; 
        </code>
      </pre>
      <br>
<h4 id="put"> PUT Request </h4>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
          &lt;button hx-put=&quot;https://html-mock.fly.dev/tag/paragraph&quot;&gt;
          Put Money In Your Account
        &lt;/button&gt;
        </code>
      </pre>
    <p> 👇 Output </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
          &lt;!-- You will always get the same response regardless of put parameters or endpoint --&gt;
          Put Request Received
        </code>
    </pre>
    <br>
    <h4 id="delete"> Delete Request </h4>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
          &lt;button hx-delete=&quot;https://html-mock.fly.dev/tag/paragraph&quot;&gt; 
          Delete your account
        &lt;/button&gt;
        </code>
      </pre>
    <p> 👇 Output </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
          &lt;!-- You will always get the same response regardless of put parameters or endpoint --&gt;
          Delete Request Received
        </code>
      </pre>
    <br>
    <h4 id="classes"> Adding classes </h4>
      <p> Simply add the class attribute to the url as a parameter. You can add as many classes as 
        you want, just make sure they are url encoded correctly. </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;button hx-get=&quot;https://html-mock.fly.dev/tag/paragraph?class=bg-dark%20text-white%20p-3&quot;&gt; 
            Get Paragraph
            &lt;/button&gt;
        </code>
      </pre>
    <p> 👇 Output </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;p class=&quot;bg-dark text-white p-3&quot;&gt; Lorem Ipsum &lt;/p&gt;
        </code>
      </pre>
    <br>
    <h4 id="own-data"> Your own data </h4>
      <p>You can return back any kind of HTML fragments you wish. Just make a github gist 
        then make a request to our server with the gist id as a parameter. </p>
      </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;button hx-get=&quot;https://html-mock.fly.dev/gist/c9fd72b8f8a265d8bfcdb4338ffc76fa&quot;&gt; 
            Get Custom HTML
            &lt;/button&gt;
        </code>
      </pre>
    <p> 👇 Output </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;p&gt; Hello, World &lt;/p&gt;
        </code>
      </pre>
    <br>


## Contributing
Contributions to the mock-html project are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
The MockHTML Server project is open-source and available under the MIT License.