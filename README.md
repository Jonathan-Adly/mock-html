<h4 id="get"> Getting a resource </h4>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;!-- any html tag can send a request in htmx --&gt;
            &lt;!-- you can use hx-get or hx-post or hx-put or hx-delete --&gt;
            &lt;!-- different swap startegy are valid --&gt;
            &lt;button
            hx-get=&quot;{{url}}tag/table&quot;
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
            &lt;form hx-post=&quot;{{url}}tag/paragraph&quot;&gt;
            &lt;label for=&quot;name&quot;&gt;Name:&lt;/label&gt;
            &lt;input type=&quot;text&quot; id=&quot;name&quot; name=&quot;name&quot; value=&quot;foo&quot;&gt;
            &lt;input type=&quot;submit&quot; value=&quot;Submit&quot;&gt;
            &lt;/form&gt;
        </code>
      </pre>
    <p> 👇 Output </p>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
            &lt;p&gt; Lorem Ipsum &lt;/p&gt; You Posted the following values: foo
        </code>
      </pre>
      <br>
<h4 id="put"> PUT Request </h4>
    <pre class="bg-dark text-white p-3">
        <code class="language-html">
          &lt;button hx-put=&quot;{{url}}tag/paragraph&quot;&gt;
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
          &lt;button hx-delete=&quot;{{url}}tag/paragraph&quot;&gt; 
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
            &lt;button hx-get=&quot;{{url}}tag/paragraph?class=bg-dark%20text-white%20p-3&quot;&gt; 
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
            &lt;button hx-get=&quot;{{url}}gist/c9fd72b8f8a265d8bfcdb4338ffc76fa&quot;&gt; 
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