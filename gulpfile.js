const gulp =require("gulp"),
sass=require('gulp-sass')(require('sass')),
autoprefixer=require("gulp-autoprefixer");

gulp.task("sass",function(){
    return gulp.src("sass/scss/*.scss")
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest("public/css"))
});

gulp.task("default",function(){
    return gulp.watch("sass/scss/*.scss",gulp.series("sass"));
});

