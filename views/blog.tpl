% rebase('base.tpl')
<div class="col-sm-8 blog-main">
  % for entry in posts:
  <div class="blog-post">
    <h2 class="blog-post-title">{{entry['TITLE']}}</h2>
    <p class="blog-post-meta">{{entry['POST_DATE']}} by <a href="#">{{entry['AUTHOR']}}</a></p>

    <p>{{entry['CONTENT']}}</p>
  </div><!-- /.blog-post -->
  % end
  <nav class="blog-pagination">
    <a class="btn btn-primary" href="#">Older</a>
    <a class="btn btn-secondary disabled" href="#">Newer</a>
  </nav>

  <div class="blog-pagination">
    <a class="btn btn-primary" href="/post">Add new entry</a>
  </div>

</div><!-- /.blog-main -->
