<?php

use App\Http\Controllers\DashboardController;
use App\Http\Controllers\DataCustomerController;
use App\Http\Controllers\DataSparepartController;
use App\Http\Controllers\DataServiceController;
use App\Http\Controllers\DataPembelianController;
use App\Http\Controllers\DataTransaksiController;
use App\Http\Controllers\RincianBiayaController;
use App\Http\Controllers\DataServisPanggilanController;
use App\Http\Controllers\LaporanController;
use App\Http\Controllers\UserController;
use App\Http\Controllers\ServisPanggilanController;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\DashboardUserController;
use GuzzleHttp\Middleware;
use SebastianBergmann\CodeCoverage\Report\Html\Dashboard;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


Route::get('/', function () {
    return view('welcome');
});
// Route::resource('/datacustomer', DataCustomerController::class)->middleware('auth', 'isAdmin');
// Route::resource('/datapegawai', UserController::class)->middleware('auth');

Route::get('/dashboarduser',[App\Http\Controllers\DashboardUserController::class,'index'])->middleware('auth')->name('indexuser');
Route::resource('/rincianbiaya', RincianBiayaController::class);
Route::resource('/datasparepart', DataSparepartController::class);
Route::resource('/dataservice', DataServiceController::class);
Route::resource('/servispanggilan', ServisPanggilanController::class);
Route::resource('/dataservispanggilan', DataServisPanggilanController::class);
// Route::get('/laporan', [LaporanController::class,'index'])->middleware('auth')->name('laporan');
// Route::post('/laporan/cetak', [LaporanController::class,'cetak'])->middleware('auth');

Route::middleware(['isAdmin', 'auth'])->group(function(){
    Route::resource('/datacustomer', DataCustomerController::class);
    Route::resource('/datapegawai', UserController::class);
    Route::resource('/dashboard',DashboardController::class);
    Route::resource('/dataservice', DataServiceController::class);
    Route::resource('/service', DataServiceController::class);
    Route::resource('/pembelian', DataPembelianController::class);
    Route::resource('/datasparepart', DataSparepartController::class);
    Route::get('/laporan', [LaporanController::class,'index']);
Route::post('/laporan/cetak', [LaporanController::class,'cetak']);

});

Auth::routes();
Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');
Route::get('/AboutUs', [App\Http\Controllers\AboutUsController::class, 'index'])->name('AboutUs');
Route::get('/Contact', [App\Http\Controllers\ContactController::class, 'index'])->name('Contact');

// Route::get('/home',[\App\Http\Controllers\LandingController::class,'index'])->name('welcome')