@extends('layoutuser.main')

@section('content')                      
    <!-- Begin Page Content -->
    <div class="container-fluid">

        <!-- Page Heading -->
        <h1 class="h3 mb-2 text-gray-800">Rincian Biaya</h1>
        <p class="mb-4">Anda dapat menghitung Rincian Biaya</p>

      @if(Session::has('berhasil'))
          <div class="alert alert-success">
              <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <strong>Success,</strong>
              {{ Session::get('berhasil') }}
          </div>
      @endif
        <!-- DataTales Example -->
        <div class="card shadow mb-4">
          <div class="card-body">
              <a href="/rincianbiaya/create" class="btn mb-3 btn-primary btn-icon-split btn-sm">Tambah Rincian Biaya</a>
            <div class="table-responsive">
              <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                <thead>
                  <tr>
                    <th>Id Rincian</th>
                    <th>Service</th>
                    <th>Sparepart</th>
                    <th>Biaya</th>

                  </tr>
                </thead>
                <tbody>
                  
                  @foreach ($rincianbiaya as $rinciannya)
                  <tr>
                    <td>{{$loop -> iteration}}</td>
                    <td>{{$rinciannya->service->nama}}</td>
                    <td>{{$rinciannya->sparepart->nama}}</td>
                    <td>{{$rinciannya->biaya}}</td>
                  </tr>
                  @endforeach
                </tbody>
              </table>
              {!!@$rincianbiaya->links()!!}
            </div>
          </div>
        </div>
      </div>
      <!-- /.container-fluid -->
</div>
</div>       
@endsection